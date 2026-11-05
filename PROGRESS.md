# Progress — רחפנים בשירות הפארק

Claude keeps this file up to date. Every session starts by reading it and ends
by updating it, so work can stop and resume at any point.

**Now:** Phase 0 · setup done, version check done — waiting for the developer to confirm folder, inputs and the version-check result
**Waiting on you:** confirm the setup (see the message in chat), and say whether the design/storyboard differences below are OK to go on with
**Waiting on others:** nothing yet

## Inputs
- Storyboard: `../../סטם_רחפנים_אחרי עריכה לשונית ולאחר הערות פיקוח.pptx` (file date 2026-11-05; "after language edit and after supervision comments"). 33 slides, 7 questions.
- PSD: `../../stem_drones.psd` (file date 2026-11-03). 16 frames. Never copied into the project.
- Design comps: `../../transfer-01a1a149/drones_03.11.26_v2.pptx` (file date 2026-11-03, 18 frames). Same content as the PSD.
- Applets (HTML, from the content team): `../../יישומונים/` — `שאלה 1 - מיון צילומי רחפנים.html`, `שאלה 4 - מיון צילומי רחפנים.html`, `מרכז הבקרה.html`
- Videos: placeholders only for now (decision from the developer, 2026-11-05).
- Project slug `park-drones`, translation prefix `PARKDRONES`. Preview: `park-drones` in the opened folder's `.claude/launch.json`, port 8134.

## Version check (storyboard vs design) — 2026-11-05
- Same structure: 7 questions, same numbering, same stems. The design was made **before** the storyboard's last round (PSD/comps 3 Nov, storyboard 5 Nov, after the supervision comments).
- Differences found (learner text comes from the storyboard, looks from the PSD):
  1. **Slide 24 (screen after Q5):** design says "הוא עמד במשימה של צילום **167** התמונות"; storyboard says **142** (and 142 is the right answer of Q5, so the storyboard is the consistent one).
  2. **Question 6:** design = one sentence, "דרגו את המדד המתאים", with a single drop target and 4 buttons (גדל / קטן / נשאר / אף אחד מהמדדים); storyboard = "פחות מ 15 תמונות", 4 metrics (השכיח, הממוצע, החציון, הטווח), each gets a card (גדל / קטן / נשאר ללא שינוי) from an unlimited stack. The layout must be adapted.
  3. Design Q6 says "רק 12 תמונות"; storyboard says "פחות מ 15 תמונות".
  4. Other small wording differences are expected; they are listed in Phase 2.

## Phases
- [x] 0 · Setup — inputs found, tools installed, project folder created
- [ ] 1 · Storyboard read — screen map (screens.json, PROJECT_BRIEF.md), production-notes.md, open-questions.md
- [ ] 1 · ✋ Developer reviewed the screen map; open questions sent (date: )
- [ ] 2 · Design reference — PSD inventory, frames mapped to screens, mockups for the overlay
- [ ] 3 · ASSET_CHECKLIST.md written
- [ ] 3 · ✋ Assets exported by the developer and checked (check_assets.py clean)
- [ ] 4 · Screens built (tick per batch below)
- [ ] 5 · Applets built and signed off; videos and audio in
- [ ] 6 · Self-QA passed (qa_check.py 0 errors, walk-through done)
- [ ] 7 · Translation export done (both sweeps pass), ASSET_LOCALIZATION.md written
- [ ] 8 · ✋ Delivered: repo pushed (published to the org the first time), SharePoint shortcut and snapshot updated, links sent

## Screens
| # | sid | built | matches design | approved by developer |
|---|---|---|---|---|
| 1 | intro | ☐ | ☐ | ☐ |

(The demo screen list above is the starter's; the real list comes in Phase 1.)

## Decisions
- 2026-11-05 · Videos are placeholders for now (`data-pending-asset`); real files later. · developer

## Open items
- The three HTML applets in `../../יישומונים/` must be checked in Phase 5 (self-contained? gating? which screens).

## Delivery log
<!-- date · git commit · repo link · SharePoint link · what changed since the last one -->
