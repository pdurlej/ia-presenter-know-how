# Complete Example — Patterns That Don't Look Like PowerPoint

> A larger iA Presenter deck that demonstrates the full syntax in this corpus while staying a real deck: assertive titles, a visible surface that carries meaning, speaker notes that sound spoken, and a close that lands.
>
> Read it two ways — as a syntax catalog, and as a model of how a good deck is shaped. Every indented line uses a real TAB.

---

# Your Slides Are Fighting Your Talk
## How iA Presenter syntax keeps them on the same side

This is the cover: a `#` title and a `##` subtitle. I open with the tension the whole deck resolves — most tools make you design first and think later, and the slides end up competing with the speaker.

---

## Headings carry the slide

Every heading is automatically visible to the audience — no TAB needed. Body text is different: it only shows if I indent it with a TAB.

`# Title` and `## Subtitle` build the cover

`## Slide Title` titles a content slide

`---` starts a new slide

This is the one mental model that makes everything else click, so I slow down here.

---

## Speech and slide, side by side in one file

This flush-left line is speech — only I see it. The next indented line is what the room sees.

	This text appears on the slide.

Back to speech again. I never copy my notes onto the slide; I promote only the line that deserves to be seen.

---

## Emphasis, used sparingly

Inline formatting works, but on a slide a little goes a long way.

	**Bold** for the one word that matters

	*Italic* for a lighter, quieter shift

	`inline code` when the literal token is the point

If everything is bold, nothing is.

---

## Lists earn their shape

Ordered when sequence matters:

	1. First this
	2. Then this
	3. Then this

Unordered when the items are siblings, not steps:

	- One angle
	- Another angle
	- A third angle

I reach for a list because the relationship is real, not to fill the slide.

---

## Let the quote do the talking

A customer or expert voice lands harder than my paraphrase. I read the room, then let it sit.

	> "The only way to learn to speak is to speak."
	> — Dale Carnegie

I add a line that says what to do with the quote.

---

## Links point somewhere real

When a link belongs on the slide, indent it so the audience sees it.

	[Read the iA Presenter how-to](https://ia.net/presenter/how-to)

Otherwise keep the URL in your notes and just say where it leads.

---

## Stacked is the honest default

When each point sharpens the one before it, let the slide stack vertically.

	The problem feels like volume.

	It's actually delay.

	Delay is what breaks trust.

Stacking shows the argument building, one beat at a time.

---

## Split only for real contrast

Two indented blocks separated by a blank line WITHOUT a TAB sit side by side. I use it only when the comparison is the message.

	Before
	Slow, manual, anxious

	After
	Fast, assisted, confident

The blank separator line must have no TAB, or the blocks stack instead.

---

## Three columns when the set is the point

	Discover
	Talk to users

	Decide
	Pick one bet

	Ship
	Put it in front of people

Three is usually the limit before a slide stops breathing.

---

## A heading stack reads in one glance

### The queue is not the problem

#### The handoff is

No TABs here — headings are visible by default. I use `###` for the main thought and `####` for the turn or qualifier. Great for a fast rhetorical beat with no list at all.

---

## One image, one job

![A wide, calm landscape](/assets/landscape.jpg)

A picture should advance the argument, not decorate it. The image is flush-left and the path starts with `/` — both are required, and the file has to be bundled in the package or nothing appears.

---

## An image alone owns the slide

![A quiet street at dawn](/assets/scene.jpg)

When an image is the only thing in its cell, it fills the slide. That is the strongest visual move iA Presenter gives me, and it costs one line. I say the point out loud instead of writing it on top of the picture.

---

## A caption when the picture needs a name

/assets/diagram.jpg "How the three parts fit together"

A bare path with a caption in straight quotes is the content-block form. Use it when the audience needs to know *what* they are looking at.

---

## Code when the code is the message

```python
def greet(name):
    print(f"Hello, {name}!")
```

For a technical room, the snippet is the slide. I keep it short enough to read from the back.

---

## A tiny table for exact deltas

| Metric | Before | Target |
|--------|--------|--------|
| First response | 11h | < 3h |
| Escalations | 27% | < 15% |

A table only when the grid itself is the point. Three rows beat three slides; ten rows beat the audience into submission.

---

## Same surface, two sides

### Reading from slides

#### Kills attention

### Talking to people

#### Earns it

A clean contrast can be built from headings alone — no list, no table, no split needed.

---

# Write the talk. The deck follows.

I close on the through-line, not a recap. If the room remembers one sentence, I want it to be this one.

---

## What to do next

	1. Open a new deck
	2. Write your script flush-left
	3. Promote one line per slide with a TAB

Questions come after the landing, never instead of it.
