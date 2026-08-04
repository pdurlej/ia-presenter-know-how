# Accent probe

## This word is **bold**

E2 — this deck is set to the dark preset and contains exactly one bold word.

Temporarily set `DarkAccent1: "#00FF00"` and `LightAccent1: "#FF00FF"` in `themes/Broadsheet/presets.json`, reload, and look at the bold word above.

Green → `DarkAccent1` means the accent for dark **mode**. The shipped CSS is correct; put the real hexes back.

Magenta → `DarkAccent1` means a dark-**coloured** accent used in light mode. Swap the two `--sig-accent` lines in section 11 of `broadsheet.css`, then put the real hexes back.

Either way the shipped colours clear 3:1 in both modes, so a wrong guess is a slightly weaker accent, never an unreadable one.
