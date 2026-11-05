# Progress — רחפנים בשירות הפארק

Claude keeps this file up to date. Every session starts by reading it and ends
by updating it, so work can stop and resume at any point.

**Now:** Phases 2–4 first pass · all 16 screens styled to the PSD (panel, pills, help/check/arrow buttons, banners, backgrounds, animations); applets and videos still placeholders — waiting for the developer's visual review and the answers to open-questions.md
**Waiting on you:** look at the screens (preview, or `index_dev.html` with "compare with design"), then go over open-questions.md together
**Waiting on others:** designer: 12–14 (not sent); content team: 1–11 (not sent)

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
- [x] 2 · Design reference — PSD inventory, frames mapped to screens, mockups for the overlay
- [x] 3 · ASSET_CHECKLIST.md written
- [x] 3 · Assets exported from the PSD by Claude and checked (check_assets.py: 0 errors, 0 warnings; contact sheet looked at)
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
- 2026-11-05 · Screen 14 (party) opening is the generated clip `assets/videos/party-huddle.mp4` (MiniMax via Hedra, reversed with the ffmpeg bundled in the imageio-ffmpeg Python package). Screens 10 and 12 will get clips the same way later. · developer + Claude
- 2026-11-05 · Slides 29 and 32 are animations with sound and no PLAY button (open question 11). Sound starts with the screen and has a mute button; an exception to the house no-autoplay-sound rule, decided by the developer. Slide 29 and 32 carry a hidden descriptive text for screen readers. Sounds are synthesized stand-ins. · developer
- 2026-11-05 · Every math expression shows left to right as in English (sums, equations, fractions), forced with `<span class="eq">`. Because of that two sums are written in the page in the order they show: "140 - 110 = 30" (storyboard text "30 = 110 - 140") and "650 ÷ 5 = 130" ("130 = 5 ÷ 650"). Intentional; the text check reports them. Number lists (inside sentences and the sorted lines in the feedback) keep Hebrew order: first number at the right. · developer (open question 9)
- 2026-11-05 · Feedback titles stay "צדקת!" / "זו טעות" and the check button stays "צדקתי?", as in the storyboard. · developer (open question 10)
- 2026-11-05 · Open questions 1–8 answered by the developer: (1) arrow after 3 s on the first screen; (2) PLAY appears after 3 s on both videos (to build); (3) "(צוחק)" stays out of the captions; (4) only the typed range and median are graded in question 1, and only the chosen option in question 3; (5) alt text for the corrected log as suggested; (6) question 1 scores only when both boxes are right; (6b) the lomda sends only the grade, the system decides pass/fail; (8) "7." added to question 7. · developer
- 2026-11-05 · Question 7 (control center): the arrow appears when the applet reaches its final "תוכנית הפריסה אושרה" state, whether the learner solved it or the applet showed the answer after the second wrong try. The applet must post a "task completed" message at that point. · developer
- 2026-11-05 · Question 7's stem gets the number "7." in front (the storyboard left it out; the other six have theirs). · developer
- 2026-11-05 · The white question panel is the PSD's (outer box 18,18 to 1902,1062, 4 px black edge, radius 44), not the house 1800×798 panel. House text sizes stay (40/34/46). The progress pills, help button, check button and arrows are the PSD's size and place; the banner is the PSD's translucent card flush top-right. · developer (storyboard/design rule) + Claude
- 2026-11-05 · At the house text sizes the PSD's question layouts do not fit with a feedback box, so per screen: pictures/applets of Q1, Q2, Q3, Q5 are scaled down (about 0.85 / 0.65 / 0.7 / 0.8) and the feedback box sits in free white space. An automatic overlap test (feedback vs text, pictures, buttons, help button) passes for every question in retry, wrong and correct states; the check button is inside the panel on every question. · Claude
- 2026-11-05 · Wrong-answer titles stay purple (house rule), the design's older coral title is not used. · Claude
- 2026-11-05 · All seven question screens share one background (`bg-question.jpg`); the PSD frames are identical there. · Claude
- 2026-11-05 · Storyboard = source of truth for text and behaviour; design (PSD) = source of truth for looks. · developer
- 2026-11-05 · Question weights: equal (the storyboard's slide-33 note), written as 14.2857 each so they add up to 100. · Claude, from the storyboard
- 2026-11-05 · The first screen is an `explain` screen (a blinking arrow after a few seconds, no start button, no back arrow). · Claude
- 2026-11-05 · Question stems follow the storyboard ("N." inside the text), not the design's "שאלה N:" heading. Check button reads "צדקתי?" and the wrong title "זו טעות", as the storyboard has them. · Claude (open questions 8, 10)
- 2026-11-05 · Videos are placeholders for now (`data-pending-asset`); real files later. · developer

## Open items
- Phase 4 batch 1 built, not yet approved by the developer (screens table below stays unticked until he says so).
- Question 4: the PSD has Lihi at x 560; moved to x 160 so the stem column does not cross her.
- Videos: posters are exported (video-test-poster, video-typo-poster); no video files yet.
- control-center: striped applet placeholder over the monitor; the monitor's start card (Hebrew painted in the PSD) comes with the applet in phase 5. `control-center-icons.png` is exported and waits for it.
- party: animation is CSS (kids zoom in, flash, phone rises); no sound yet (open question 11).
- Caption times in both videos are placeholders (spread evenly); replace with the SRT when the real videos come.
- The PLAY delay (3 s) and the control-center completion gate need small build pieces (HOOKs), not engine changes.
- Q6 needs an endless-stack look for the cards (four copies of each are in the bank).
- The three HTML applets in `../../יישומונים/` must be checked in Phase 5 (self-contained? gating? which screens).

## Delivery log
<!-- date · git commit · repo link · SharePoint link · what changed since the last one -->
