# iA Presenter Intake

Ask only for information that materially changes the deck.

## Minimal Questions

1. Who is the audience?
2. What should they understand, believe, or decide?
3. What should happen after the presentation?
4. How long is the talk, or how many slides should it roughly be?
5. What tone should it have?
6. Is there real evidence or data that must appear?
7. Are real photos available? If not, backgrounds are generated with `tools/genbg.py` — a deck is never shipped image-free.
8. Are there hard constraints or taboo topics?

## Safe Defaults

- audience: educated non-specialist unless context says otherwise
- objective: understand and accept the main proposition
- CTA: agree to the next concrete step after the presentation
- duration: 10-15 minutes
- deck size: 8-12 core slides
- tone: clear, confident, human
- evidence: no hard data unless provided
- visuals: image-backed by default — full-bleed image on the opener, the closer, and each narrative turn; generate backgrounds with `tools/genbg.py` when no photos are supplied
- constraints: none unless user gives them

## Notes

- If the user already gave enough information, do not re-ask the whole intake.
- If only one thing is missing, ask only that one thing.
- If the user does not answer, apply defaults and state them briefly in the final response.
- Candidate mode can start with defaults; final expansion should tighten assumptions if needed.
