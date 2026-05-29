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
