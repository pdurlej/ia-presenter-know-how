# Image Sourcing

Use this when the deck needs real visuals and the user has not provided assets.

## Principle

Images should strengthen the story, not replace it.

Good reasons to source an image:
- open a section with mood or scene
- create contrast after several text-led slides
- show a concrete environment, object, or workflow

Bad reasons:
- the slide feels empty
- the deck needs decoration
- the message is still unclear

## Default Sources

Prefer:
- Unsplash
- Pexels

These are useful because they are searchable, broad, and easy to integrate late in the workflow.

## Query Style

Search for:
- concrete scenes
- work contexts
- moods
- physical environments

Prefer:
- `operations team dashboard`
- `warehouse scanner hand`
- `customer support office night`
- `procurement meeting laptop`

Avoid vague prompts like:
- `innovation`
- `future`
- `technology background`

## Matching Image to Slide Job

Use one of these intents:
- scene-setting
- tension
- proof of real-world context
- break in rhythm
- chapter reset

The image query should describe the intent, not only the noun.

Example:
- not just `finance`
- better: `finance team review meeting spreadsheet laptop`

## Workflow

1. Draft the story first.
2. Mark where an image would genuinely help.
3. Search Unsplash or Pexels only after structure is stable.
4. Shortlist 2-4 candidates per slot.
5. Prefer images that survive responsive cropping.
6. Add the asset late and adjust position or background behavior.

## Technical Support

This skill includes a helper:

```bash
python3 skills/ia-presenter-deck/scripts/search_stock_images.py --query "customer support team office" --provider all --count 5
```

Behavior:
- if `PEXELS_API_KEY` and/or `UNSPLASH_ACCESS_KEY` are set, the script queries the official APIs
- if keys are missing, it prints official site search URLs you can open manually

## Provider Notes

### Unsplash

- The official API supports photo search.
- Unsplash requires hotlinking the image URLs returned by the API when displaying exact source images from the API.
- Attribution is required for API uses and appreciated more broadly.

### Pexels

- The official API supports photo search.
- Pexels asks for a prominent link back to Pexels and encourages photographer credit when possible.
- Do not use the API to replicate a competing photo library.

## Safety and Quality Checks

Before putting a stock image into a deck, ask:
- Does it carry the right mood without becoming generic?
- Will the important subject survive cropping on smaller screens?
- Does it look like a real context instead of a cliché?
- Does it accidentally reveal branding, trademarks, or misleading UI?
- Is there a stronger no-image solution for this slide?

## Working Rule

One strong image every few slides is usually more effective than turning the deck into a stock-photo gallery.
