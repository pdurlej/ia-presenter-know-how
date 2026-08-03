#!/usr/bin/env python3
"""ialint - a linter for iA Presenter decks.

Checks an .iapresenter package (or a bare text.md / .md file) for mistakes that
either render incorrectly in iA Presenter or weaken the deck. Every rule is
grounded in live testing on iA Presenter, not guesswork.

Usage:
    python3 tools/ialint.py DECK.iapresenter [MORE ...]
    python3 tools/ialint.py path/to/text.md
    python3 tools/ialint.py --help

Exit code: 1 if any ERROR-level finding, else 0. Use --strict to also fail on
warnings.

Suppressing rules (for files that are deliberately wrong, e.g. an anti-pattern
catalogue):

    <!-- ialint-disable -->               disable every rule in this file
    <!-- ialint-disable E001,W106 -->     disable only these codes in this file
    <!-- ialint-disable-next-line E001 -->  disable for the following line only

Put the comment anywhere in the file; it is an HTML comment, so it stays
invisible in rendered Markdown and in iA Presenter.

Rule reference:
  ERRORS (deck renders wrong)
    E001  table row is TAB-indented  -> renders as a code block, not a grid
    E002  fenced code block is TAB-indented -> the fence breaks
    E003  image path is not root-relative (missing leading "/") -> won't render
    E004  image uses a remote http(s) URL -> iA Presenter won't fetch it
    E005  image path "/assets/..." has no matching file in the package
  WARNINGS (renders, but weaker)
    W101  image has empty alt text -> may render as literal text; add alt/caption
    W102  image line is TAB-indented -> keep images flush-left
    W103  line indented with spaces -> use a real TAB for slide content
    W104  deck ends on "Thank you" / "Questions" -> close on an action instead
    W105  generic slide title (Overview, Agenda, Conclusion ...) -> make it assert
    W106  more than 6 list items in one block -> too many bullets
  PACKAGE
    E010  package is missing text.md
    E011  info.json is missing or not valid JSON
    W110  info.json has no template / preset
"""
from __future__ import annotations
import json
import os
import re
import sys

IMG_RE = re.compile(r'!\[(?P<alt>[^\]]*)\]\((?P<path>[^)\s]+)(?:\s+"[^"]*")?\)')
BARE_IMG_RE = re.compile(
    r'^(?P<lead>[ \t]*)(?P<path>/?[\w./-]+\.(?:png|jpe?g|gif|webp|svg|mov|mp4))'
    r'(?:\s+"[^"]*")?\s*$', re.IGNORECASE)
TABLE_TAB_RE = re.compile(r'^\t+[ \t]*\|.*\|')
CODE_TAB_RE = re.compile(r'^\t+[ \t]*(```|~~~)')
FENCE_RE = re.compile(r'^(```|~~~)')
HEADING_RE = re.compile(r'^(#{1,6})\s+(?P<text>.+?)\s*$')
LIST_RE = re.compile(r'^\t+[ \t]*([-*+]|\d+\.)\s+\S')
SPACE_INDENT_RE = re.compile(r'^ {1,}\S')
CLOSING_RE = re.compile(r'\b(thank you|thanks|questions\??|q\s*&\s*a)\b', re.IGNORECASE)
DISABLE_NEXT_RE = re.compile(r'<!--\s*ialint-disable-next-line(?:\s+([A-Za-z0-9,\s]+?))?\s*-->')
DISABLE_FILE_RE = re.compile(r'<!--\s*ialint-disable(?!-next-line)(?:\s+([A-Za-z0-9,\s]+?))?\s*-->')
GENERIC_TITLES = {
    "overview", "agenda", "introduction", "intro", "conclusion", "summary",
    "background", "key metrics", "next steps", "solution overview", "about us",
    "thank you", "questions",
}

LEVEL_ERROR = "ERROR"
LEVEL_WARN = "WARN"


def _codes(group: str | None) -> set[str]:
    """Parse the code list of an ialint-disable directive; bare directive = all."""
    if not group or not group.strip():
        return {"*"}
    return {c.strip().upper() for c in group.split(",") if c.strip()}


class Finding:
    __slots__ = ("line", "code", "level", "msg")

    def __init__(self, line, code, level, msg):
        self.line = line
        self.code = code
        self.level = level
        self.msg = msg


def lint_text(md: str, bundled: set[str] | None = None) -> list[Finding]:
    """Lint the Markdown body of a deck. `bundled` is the set of file paths
    present in the package (root-relative, e.g. "/assets/x.png"); pass None to
    skip the bundled-file existence check (E005)."""
    out: list[Finding] = []
    lines = md.split("\n")
    in_fence = False
    list_run = 0
    list_run_start = 0
    last_visible = None  # (lineno, text) of last heading or tabbed line

    # Pre-pass: collect ialint-disable directives.
    file_disabled: set[str] = set()
    line_disabled: dict[int, set[str]] = {}
    for i, raw in enumerate(lines, start=1):
        m = DISABLE_NEXT_RE.search(raw)
        if m:
            line_disabled[i + 1] = _codes(m.group(1))
            continue
        m = DISABLE_FILE_RE.search(raw)
        if m:
            file_disabled |= _codes(m.group(1))

    def flush_list(end_line):
        nonlocal list_run, list_run_start
        if list_run > 6:
            out.append(Finding(list_run_start, "W106", LEVEL_WARN,
                               f"{list_run} list items in one block; keep it to ~6 or fewer"))
        list_run = 0

    for i, raw in enumerate(lines, start=1):
        # fenced code block tracking (flush-left fences toggle; tabbed fence is E002)
        if CODE_TAB_RE.match(raw):
            out.append(Finding(i, "E002", LEVEL_ERROR,
                               "fenced code block is TAB-indented; keep it flush-left or the fence breaks"))
        if FENCE_RE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        stripped = raw.strip()

        # list-run tracking
        if LIST_RE.match(raw):
            if list_run == 0:
                list_run_start = i
            list_run += 1
        elif stripped == "":
            pass  # blank lines don't break a list run for our purposes
        else:
            flush_list(i)

        # E001 tab-indented table
        if TABLE_TAB_RE.match(raw):
            out.append(Finding(i, "E001", LEVEL_ERROR,
                               "table row is TAB-indented; iA renders it as code, not a grid (keep tables flush-left)"))

        # images via markdown ![alt](path)
        for m in IMG_RE.finditer(raw):
            path = m.group("path")
            alt = m.group("alt")
            _check_image_path(out, i, path, bundled)
            if alt.strip() == "":
                out.append(Finding(i, "W101", LEVEL_WARN,
                                   "image has empty alt text; add alt (it also shows as the caption)"))
            if raw.startswith("\t"):
                out.append(Finding(i, "W102", LEVEL_WARN,
                                   "image line is TAB-indented; keep images flush-left"))

        # bare content-block image line (path on its own line)
        bm = BARE_IMG_RE.match(raw)
        if bm and not IMG_RE.search(raw) and not stripped.startswith(("|", ">", "-", "*")):
            path = bm.group("path")
            if bm.group("lead").startswith("\t"):
                out.append(Finding(i, "W102", LEVEL_WARN,
                                   "image line is TAB-indented; keep images flush-left"))
            _check_image_path(out, i, path, bundled)

        # W103 space indentation for would-be slide content
        if SPACE_INDENT_RE.match(raw) and not stripped.startswith(("-", "*", "+", ">", "[", "#", "|")):
            out.append(Finding(i, "W103", LEVEL_WARN,
                               "line is indented with spaces; use a real TAB for slide content"))

        # headings: generic-title check + track last visible
        hm = HEADING_RE.match(raw)
        if hm:
            text = hm.group("text")
            last_visible = (i, text)
            if text.strip().lower().rstrip("?.!") in GENERIC_TITLES:
                out.append(Finding(i, "W105", LEVEL_WARN,
                                   f'generic slide title "{text}"; make it assert something'))
        elif raw.startswith("\t") and stripped:
            last_visible = (i, stripped)

    flush_list(len(lines))

    # W104 weak closing
    if last_visible and CLOSING_RE.search(last_visible[1]):
        out.append(Finding(last_visible[0], "W104", LEVEL_WARN,
                           'deck ends on "Thank you / Questions"; close on a concrete action or landing line'))

    def suppressed(f: Finding) -> bool:
        if "*" in file_disabled or f.code in file_disabled:
            return True
        here = line_disabled.get(f.line)
        return bool(here) and ("*" in here or f.code in here)

    return [f for f in out if not suppressed(f)]


def _check_image_path(out, line, path, bundled):
    low = path.lower()
    if low.startswith(("http://", "https://")):
        out.append(Finding(line, "E004", LEVEL_ERROR,
                           "image uses a remote URL; iA Presenter won't fetch it - bundle the file and use /assets/..."))
        return
    if not path.startswith("/"):
        out.append(Finding(line, "E003", LEVEL_ERROR,
                           f'image path "{path}" is not root-relative; use a leading slash, e.g. /assets/{os.path.basename(path)}'))
        return
    if bundled is not None and path not in bundled:
        out.append(Finding(line, "E005", LEVEL_ERROR,
                           f'image "{path}" is not bundled in the package'))


def collect_bundled(pkg_dir: str) -> set[str]:
    """Return the set of root-relative file paths inside a package dir."""
    found = set()
    for root, _dirs, files in os.walk(pkg_dir):
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), pkg_dir)
            found.add("/" + rel.replace(os.sep, "/"))
    return found


def lint_package(path: str) -> tuple[list[Finding], str]:
    """Lint a .iapresenter package directory. Returns (findings, label)."""
    out: list[Finding] = []
    text_md = os.path.join(path, "text.md")
    info_json = os.path.join(path, "info.json")
    if not os.path.isfile(text_md):
        out.append(Finding(0, "E010", LEVEL_ERROR, "package is missing text.md"))
        return out, path
    if not os.path.isfile(info_json):
        out.append(Finding(0, "E011", LEVEL_ERROR, "package is missing info.json"))
    else:
        try:
            with open(info_json, encoding="utf-8") as f:
                info = json.load(f)
            block = info.get("net.ia.presenter", {})
            if not block.get("template") and not block.get("preset"):
                out.append(Finding(0, "W110", LEVEL_WARN,
                                   "info.json has no template/preset; the deck falls back to the default theme"))
        except (json.JSONDecodeError, OSError) as e:
            out.append(Finding(0, "E011", LEVEL_ERROR, f"info.json is not valid JSON: {e}"))
    bundled = collect_bundled(path)
    with open(text_md, encoding="utf-8") as f:
        out.extend(lint_text(f.read(), bundled=bundled))
    return out, text_md


def lint_path(path: str) -> tuple[list[Finding], str]:
    if os.path.isdir(path):
        return lint_package(path)
    with open(path, encoding="utf-8") as f:
        return lint_text(f.read(), bundled=None), path


def main(argv):
    args = [a for a in argv if not a.startswith("-")]
    strict = "--strict" in argv
    if "--help" in argv or "-h" in argv or not args:
        print(__doc__)
        return 0 if "--help" in argv or "-h" in argv else 2

    total_err = total_warn = 0
    for target in args:
        if not os.path.exists(target):
            print(f"{target}: not found", file=sys.stderr)
            total_err += 1
            continue
        findings, label = lint_path(target)
        findings.sort(key=lambda f: (f.line, f.code))
        if findings:
            print(f"\n{label}")
            for f in findings:
                loc = f"{f.line}" if f.line else "-"
                print(f"  {label}:{loc}: [{f.code}] {f.level}: {f.msg}")
        errs = sum(1 for f in findings if f.level == LEVEL_ERROR)
        warns = sum(1 for f in findings if f.level == LEVEL_WARN)
        total_err += errs
        total_warn += warns

    print(f"\nialint: {total_err} error(s), {total_warn} warning(s)")
    if total_err or (strict and total_warn):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
