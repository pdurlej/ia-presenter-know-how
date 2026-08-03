# Tools

## `ialint.py` — iA Presenter deck linter

A dependency-free linter (Python 3 stdlib only) that checks an `.iapresenter`
package or a bare `text.md` for mistakes that render incorrectly in iA Presenter
or weaken the deck. Every rule is grounded in live testing on iA Presenter, not
guesswork — it is the automated form of the hard-won findings in
`syntax/00-complete-reference.md` and `examples/03-anti-patterns.md`.

### Usage

```bash
python3 tools/ialint.py path/to/deck.iapresenter
python3 tools/ialint.py path/to/text.md
python3 tools/ialint.py golden-candidates/*.iapresenter
```

Exit code is `1` when any ERROR is found, else `0`. Add `--strict` to also fail
on warnings (useful in CI).

### What it catches

**Errors — the deck renders wrong:**

| Code | Problem |
|------|---------|
| E001 | Table row is TAB-indented → iA renders it as code, not a grid |
| E002 | Fenced code block is TAB-indented → the fence breaks |
| E003 | Image path is not root-relative (missing leading `/`) → won't render |
| E004 | Image uses a remote `http(s)` URL → iA Presenter won't fetch it |
| E005 | Image path `/assets/…` has no matching file bundled in the package |
| E010 | Package is missing `text.md` |
| E011 | `info.json` is missing or not valid JSON |

**Warnings — it renders, but weaker:**

| Code | Problem |
|------|---------|
| W101 | Image has empty alt text (alt also shows as the caption) |
| W102 | Image line is TAB-indented (keep images flush-left) |
| W103 | Line indented with spaces (use a real TAB for slide content) |
| W104 | Deck ends on "Thank you / Questions" (close on an action) |
| W105 | Generic slide title (Overview, Agenda, Conclusion …) |
| W106 | More than ~6 list items in one block |
| W110 | `info.json` has no template/preset (falls back to default theme) |

### Suppressing rules

Some files are *deliberately* wrong — an anti-pattern catalogue has to show the
broken form. Switch rules off with an HTML comment, which stays invisible both in
rendered Markdown and in iA Presenter:

```markdown
<!-- ialint-disable -->                   disable every rule in this file
<!-- ialint-disable E001,W106 -->         disable only these codes in this file
<!-- ialint-disable-next-line E003 -->    disable for the following line only
```

`examples/03-anti-patterns.md` uses the file-level form.

### Continuous integration

`.github/workflows/lint-decks.yml` runs on every pull request and on `master`:

1. unit-tests the linter (`python3 -m unittest discover -s tests`)
2. lints every example and golden candidate
3. smoke-tests `genbg.py`

The gate is **errors only** — warnings are advisory and do not fail the build.
Because the linter now decides whether the corpus is publishable, it has its own
test suite in `tests/test_ialint.py`; add a test there with any new rule.

### Why this matters for LLM-generated decks

iA Presenter abstracts visual design away from the text, so an LLM cannot "see"
the rendered slide. The linter gives it a fast, deterministic feedback loop:
generate the deck → run `ialint` → fix every ERROR → deliver. It turns rendering
rules an LLM can't observe into checks it can act on.

### The two rules worth memorizing

1. **Tables and fenced code blocks are flush-left.** A leading TAB turns them
   into code.
2. **Image paths are root-relative and bundled.** `![alt](/assets/photo.png)`
   with the file at `<package>/assets/photo.png`. No leading slash → literal
   text. Remote URL → nothing.

---

## `genbg.py` — generate abstract background images

iA Presenter won't fetch remote image URLs, and an LLM has no photos of its own.
But it *can* generate clean abstract gradient backgrounds and bundle them —
full-bleed colour and texture with zero external assets. This is the
LLM-autonomous path to making a deck feel like a presentation, not a document.

```bash
# named palette into a package's assets/ folder
python3 tools/genbg.py mydeck.iapresenter/assets --palette indigo

# custom two-colour diagonal gradient
python3 tools/genbg.py mydeck.iapresenter/assets --name cover --from 16223D --to F9615F

# list palettes
python3 tools/genbg.py --list
```

Then reference it root-relative in the deck: `![Mood](/assets/indigo.png)`.

Palettes: `indigo`, `plum`, `ink`, `teal`, `ember`, `forest`, `slate`, `gold`.
Dependency-free (stdlib only). See `references/VISUAL-DESIGN.md` for how to use
backgrounds for rhythm and section breaks.
