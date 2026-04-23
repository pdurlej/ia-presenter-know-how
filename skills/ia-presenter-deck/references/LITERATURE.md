# Presentation Literature Notes

This file translates literature into operational rules for `ia-presenter-deck`.
It is not a reading log. It exists to turn books into better deck behavior.

## Active Sources

### Nancy Duarte, `Resonate`

Local source used:
- `/Users/pd/Downloads/Resonate - Present Visual Stories That Transform Audiences -- Soundview Executive Book Summaries_;Duarte, Nancy -- Soundview Executive Book Summaries -- isbn13 9780470632017 -- 71de91423aacbde76bcd08f405e207c9.epub`

Working takeaways:
- presentations are not reports; they are experiences built from information plus story
- the audience is the hero, not the presenter
- a presentation needs a destination; every slide should move the audience toward that destination
- the core message should behave like one big idea, not a loose topic
- strong talks create contrast between the current state and the future state
- memorable presentations include a deliberate `S.T.A.R.` moment
- signal-to-noise ratio matters; remove friction that makes the message harder to receive

Rules derived for this repo:
- do not build decks as projected documents
- define audience transformation, not only topic coverage
- every deck should name one big idea before slide drafting
- contrast should be designed intentionally, not left to generic before/after phrasing
- at least one slide or sequence should act as a memorable anchor, but it must magnify the idea rather than decorate it
- remove visual or structural noise before adding more content

### Barbara Minto, `The Pyramid Principle`

Local source available:
- `/Users/pd/Downloads/The Pyramid Principle- Logic in Writing and Thinking -- Barbara Minto -- 2022 -- e13108a879dd9d05d8334aceda929db6.epub`

Current status:
- this EPUB is image-based
- targeted OCR has been used to confirm the practical principles below
- full clean extraction is still pending, but the executive-writing rules below are solid enough to encode now

Working takeaways:
- the top sentence answers a question already alive in the reader’s mind
- the opening should be structured as `Situation -> Complication -> Question -> Answer`
- communication is clearest when ordered from the top down
- each layer should directly answer the question raised by the layer above
- choose deductive structure when the conclusion is surprising or the argument itself needs defending
- choose inductive structure when grouped observations naturally lead to one insight
- grouped ideas must be genuinely related and logically ordered
- summary points must state either:
  - the effect of the actions below, or
  - the insight implied by the similar facts below
- avoid intellectually blank assertions such as `there are three reasons`, `we have five priorities`, or `there are two problems`

Rules derived for this repo:
- executive decks should answer first, then earn the answer
- every section should be able to name the question it is answering
- support slides should be grouped tightly enough that a real summary line can sit above them
- do not dump news or lists of facts without synthesizing what they imply
- when facts do not support one higher-order insight, they probably do not belong on the same slide or in the same section
- for proposals, reviews, and board updates, prefer explicit narrative logic over atmosphere

### Nancy Duarte, `slide:ology`

Local source used:
- `/Users/pd/Downloads/slidology.pdf`

Working takeaways:
- slides should support the presenter, not become a projected document
- dense text creates `Presentation-as-Document Syndrome`; it serves neither the document job nor the live-talk job well
- the audience will either read the slide or listen to the presenter; they will not comfortably do both
- slides work best as visual aids that reinforce the speaker's message
- presenters need audience awareness, not just message ownership
- good slides require visual thinking, not only bullet editing

Rules derived for this repo:
- do not let the deck drift into a slideument
- if a slide contains enough text to function alone as a memo, it is probably the wrong surface
- visible slide content must reinforce the spoken message, not compete with it
- audience-visible text should be scarce enough to read fast and strong enough to matter
- image use should sharpen a thought, not merely decorate whitespace
- if the presenter could walk away and the slide still contains the whole argument, the slide is probably overfilled

### Garr Reynolds, `Presentation Zen`

Local source used:
- `/Users/pd/Downloads/Presentation Zen 3 - simple ideas on presentation design and -- Garr Reynolds; Guy Kawasaki -- Voices that matter, Third edition, Berkeley, 2020 -- isbn13 9780135800836 -- 5f62ac031a18bba03cc2e3e9fc00b234.pdf`

Working takeaways:
- strong presentations depend on simplicity, restraint, and naturalness
- presentations are not documents; handouts and speaker notes are separate artifacts
- signal-to-noise ratio matters visually as much as verbally
- design starts early, at the stage of story and structure, not only in late styling
- visuals should be specific and meaningful; generic or staged stock weakens trust
- narrative contrast and careful sequencing are more memorable than feature dumping

Rules derived for this repo:
- remove nonessential noise before adding new surface elements
- favor one strong visual or one strong proof move over several mediocre ones
- use whitespace and scale intentionally, but do not confuse emptiness with clarity
- prefer specific images with real context over generic stock tropes
- treat tables as visual proof objects, not spreadsheet leftovers
- keep the deck human and speakable; polish should not make it feel synthetic

## How To Use These Notes

- use `Resonate` for story, audience, contrast, and memorable moments
- use `Pyramid Principle` for executive structure and argument hierarchy
- use `slide:ology` to protect the deck from becoming a projected document
- use `Presentation Zen` for simplicity, restraint, signal-to-noise, and more disciplined visuals
- when the sources conflict, keep the message logic from Minto, the audience movement from Duarte, and the restraint from Reynolds

## Immediate Implications For `ia-presenter-deck`

- stronger upfront articulation of the audience shift
- a required `big idea` before slide generation
- at least one deliberate contrast move in narrative decks
- at least one deliberate memory anchor in decks longer than 6 slides
- executive decks should default to explicit question-led top-down structure
- board and executive updates should usually use `SCQA` in the opening and `question -> answer` logic through the body
- visible slides should support the speaker, not substitute for the speaker
- a notes-heavy deck should be treated as suspect until proven otherwise
- image usage should be more selective, more contextual, and less decorative
