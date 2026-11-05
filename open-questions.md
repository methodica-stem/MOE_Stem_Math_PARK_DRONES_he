# Open questions — רחפנים בשירות הפארק

For the content team (unless it says "designer"). Each has the slide, what the
storyboard says, and what I built meanwhile. Answers go in `PROGRESS.md` →
Decisions. None of them stops the build.

## Answered (2026-11-05, by the developer)

1. Arrow after 3 seconds on the first screen.
2. PLAY after 3 seconds on both videos (still to build).
3. "(צוחק)" stays out of the captions.
4. Only the typed range and median are graded in question 1; only the chosen option in question 3.
5. Alt text for the corrected log: as suggested.
6. Question 1 scores only when both boxes are right; the lomda sends only the grade (the system decides pass/fail).
7. Control center: the arrow appears when the applet reaches its final "תוכנית הפריסה אושרה" state (solved, or shown after the second wrong try).
8. "7." added to question 7's stem.
9. Math expressions (sums, equations, fractions) show left to right as in English; number lists keep Hebrew order, first number at the right.
10. Feedback titles and the check button stay as in the storyboard.
11. Slides 29 and 32 are animations with sound, no PLAY button; slide 29 gets a descriptive alt text (built, see production-notes.md).

Still open: 12–14 (for the designer).

---

## For the content team

1. **Slide 2 — how many seconds until the blinking arrow?** The note says "after a few seconds". *Built:* 3 seconds.

2. **Slide 3 and every video — PLAY after 3 seconds.** The note says PLAY appears after 3 seconds "everywhere relevant". *Built:* PLAY shows at once for now (a build to-do, not a question). Please confirm 3 s is wanted on all videos.

3. **Slide 6 — "(צוחק)" in the speech balloon.** It is a stage direction, not spoken text. *Built:* left out of the captions (it stays in the voice-over script). Please confirm.

4. **Slide 9 — is the sorting graded?** The learner drags the numbers into order, then types the range and the median. *Suggested:* only the two typed numbers are graded, and both must be right for the question's point. The sort is a support step. The same for slide 17 (question 3, only the chosen option is graded).

5. **Slide 15 — alt text for the picture of the corrected flight log** (the note asks for it but gives no text). *Suggested:* "יומן הטיסות לאחר התיקון: הנתון 120 סומן כטעות והוחלף ב-145. שאר הנתונים: 110, 125, 130, 140."

6. **Slide 33 — grade and "בוצע בהצלחה".** The note says 70 and above is reported as "בוצע בהצלחה", with the grade. The lomda sends only the grade (0–100) at "סיימתי". *Suggested:* the system decides pass/fail from the grade. Please confirm nothing else must be sent. Also: all seven questions weigh the same (14.29 each); question 1 has two boxes — *suggested:* both right for the point.

7. **Slide 28 — what completes the control-center task?** The arrow appears only after the task is completed in the applet. Please tell me the exact end condition, or confirm the applet's own "done" state.

8. **Slides 30–31 — question 7 has no number in the stem** (the other six start "1.", "2." …). *Built:* as written. Please confirm "7." is not wanted. Also: the design's headings say "שאלה N:" for all seven; the storyboard numbering ("N.") is what I built, because the progress pills already show the number.

9. **Slides 10, 18, 23 — sums written backwards in the file.** The storyboard has them as "30 = 110 - 140", "130 = 5 ÷ 650" (plain text, so they show right when read right-to-left: 140 - 110 = 30, 650 ÷ 5 = 130). I keep them as written and check on screen how they look. Please confirm that the shown order should be "140 - 110 = 30" and "650 ÷ 5 = 130", as in the storyboard picture.

10. **Wording of the feedback titles.** The storyboard says "צדקת!" / "זו טעות". The house wording is "זו טעות, כל הכבוד על הניסיון." *Built:* as the storyboard. Also the check button is "צדקתי?" (the house default is "האם צדקתי?"). Please confirm both.

11. **Slide 32 — sound.** The note asks for the show's sound with the drone's sound on top, in the background. The house rule is no sound that starts by itself. *Suggested:* a sound button the learner presses, off by default (and the same for slide 29's flash and music). Please confirm.

## For the designer

12. **Slide 24 / PSD frame 24:** the design says the drone had to take **167** photos, the storyboard says **142**. The picture must be updated.

13. **Question 6 / PSD frame 25:** the design is the older version of the question (one sentence, one drop target, four buttons: גדל / קטן / נשאר / אף אחד מהמדדים, and "רק 12 תמונות"). The storyboard has four metrics, each with a drop place, three cards (גדל / קטן / נשאר ללא שינוי) and "פחות מ 15 תמונות". I am building the storyboard's version in the design's style. Please send the design of the four rows and the card stack, or approve what I build.

14. **Slide 11 (design note):** the characters' expressions in the designer's try don't look like them; the first picture should be the base. Is PSD frame 11 (the video's still) already updated?
