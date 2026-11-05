# Progress — רחפנים בשירות הפארק

Claude keeps this file up to date. Every session starts by reading it and ends
by updating it, so work can stop and resume at any point.

**Now:** Phase 1 · screen map and skeleton index.html done (16 screens, contract OK, text 160/161 word for word) — waiting for the developer to review the screen map
**Waiting on you:** read PROJECT_BRIEF.md (is the screen list right?) and send open-questions.md to the content team (questions 1–11) and the designer (12–14)
**Waiting on others:** content team: answers to open-questions.md 1–11; designer: 12–14 (not sent yet)

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
- [x] 1 · Storyboard read — screen map (screens.json, PROJECT_BRIEF.md), production-notes.md, open-questions.md
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
| 2 | video-test | ☐ | ☐ | ☐ |
| 3 | q1 | ☐ | ☐ | ☐ |
| 4 | video-typo | ☐ | ☐ | ☐ |
| 5 | q2 | ☐ | ☐ | ☐ |
| 6 | q3 | ☐ | ☐ | ☐ |
| 7 | next-test | ☐ | ☐ | ☐ |
| 8 | q4 | ☐ | ☐ | ☐ |
| 9 | q5 | ☐ | ☐ | ☐ |
| 10 | test-six | ☐ | ☐ | ☐ |
| 11 | q6 | ☐ | ☐ | ☐ |
| 12 | park-lights | ☐ | ☐ | ☐ |
| 13 | control-center | ☐ | ☐ | ☐ |
| 14 | party | ☐ | ☐ | ☐ |
| 15 | q7 | ☐ | ☐ | ☐ |
| 16 | finish | ☐ | ☐ | ☐ |

Phase 1 state: text and behaviour are in index.html as a skeleton (learner text word for word, the one miss is the stage direction "(צוחק)", question 3 of open-questions); no styling or positions yet; every background, video, applet and picture is a striped placeholder.

## Decisions
- 2026-11-05 · Storyboard = source of truth for text and behaviour; design (PSD) = source of truth for looks. · developer
- 2026-11-05 · Question weights: equal (the storyboard's slide-33 note), written as 14.2857 each so they add up to 100. · Claude, from the storyboard
- 2026-11-05 · The first screen is an `explain` screen (a blinking arrow after a few seconds, no start button, no back arrow). · Claude
- 2026-11-05 · Question stems follow the storyboard ("N." inside the text), not the design's "שאלה N:" heading. Check button reads "צדקתי?" and the wrong title "זו טעות", as the storyboard has them. · Claude (open questions 8, 10)
- 2026-11-05 · Videos are placeholders for now (`data-pending-asset`); real files later. · developer

## Open items
- Caption times in both videos are placeholders (spread evenly); replace with the SRT when the real videos come.
- The PLAY delay (3 s) and the control-center completion gate need small build pieces (HOOKs), not engine changes.
- Q6 needs an endless-stack look for the cards (four copies of each are in the bank).
- The three HTML applets in `../../יישומונים/` must be checked in Phase 5 (self-contained? gating? which screens).

## Delivery log
<!-- date · git commit · repo link · SharePoint link · what changed since the last one -->
