# CLI Contract

Main entrypoint:

```bash
python3 skills/ia-presenter-render/scripts/render_deck.py \
  --deck golden-candidates/02-q2-board-update.iapresenter \
  --run-dir .presentation-system/runs/q2-board-update/20260412-120000/iteration-0 \
  --mode both
```

Outputs:
- `render.json`
- `render/export-images/`
- `render/export-html/`

Failure modes:
- missing app bundle
- missing Accessibility permission for `osascript`
- UI export control not found
- export finished without files appearing in the selected folder

Expected remediation for permission failures:
- grant Accessibility access to `osascript` or the host terminal app
- retry the same command
