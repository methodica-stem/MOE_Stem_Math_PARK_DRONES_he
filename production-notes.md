# Production notes — רחפנים בשירות הפארק

From the storyboard's הפקה notes (orange callouts), per screen. Learner text found
inside notes is listed with its role. The design notes (עיצוב, purple) are
listed where they change what the screen looks like.

## Lomda-wide rules (גורף)

- **Forward arrow:** on every screen but the first, "after a few seconds a blinking arrow appears; a click moves to the next slide" (slide 2). Built: the engine's arrow, shown at once on most screens; on the opening screen after 3 s (open question 1).
- **Back arrow** on every screen after the first (slide 3).
- **PLAY button** appears after 3 seconds, wherever a video is (slide 3). Built: the engine shows PLAY at once. *To do (phase 4/5):* a 3 s delay as a screen option, not a special case in the engine.
- **Help button "עזרה"** on every question: shows and hides its help text on click (slide 9). The help texts are the grey strips at the top of each question slide. Built as `.help-btn` + `.popup-src` per question.
- **Check button "צדקתי?"** (the storyboard's label; the house default is "האם צדקתי?").
  - First mistake: **"זו אינה התשובה, נסו שוב."** + **"תוכלו ללחוץ על כפתור העזרה כדי לקבל רמז."** (retry).
  - Second mistake, or a right answer: the feedback of the slide after it.
  - The same retry text is repeated in every question's `.fb-src`.
- **Scoring (slide 33):** equal weight for all questions (7 × 14.2857 → grade out of 100). A grade of 70 or more is reported to the system as "בוצע בהצלחה", and the report includes the grade. That report is the system's job, not shown to the learner (open question 6).
- **Animations (not videos):** slides 2, 24, 27, 29, 32 each have a subtle looping or one-off animation. Slides 29 and 32 also have sound (decision 2026-11-05, open question 11): it starts with the screen, stops when the learner leaves, and a round speaker button (bottom left) mutes it. This is a deliberate exception to the house rule "no sound that starts by itself". The sound is drawn in code (Web Audio), so it is a stand-in: real recordings can replace it (put MP3s in `assets/audio` and play them from the hooks in script.js).

## Per screen

### 1 · intro (slide 2)
- Subtle animation (not a video) of the lighting changing a little in the right places. Automatic, loops.
- After a few seconds a blinking arrow appears. (3 s is my guess — open question 1.)

### 2 · video-test (slides 3–8)
- One video: slides 4–8 (the dialogue). The slide-3 banner stays over the video as a `.narration-banner`.
- Captions: the five speech balloons, one caption per line. "(צוחק)" in slide 6 is a stage direction and is left out of the captions (open question 3).
- Note to the video producer: keep the man facing the screen so that a small kippah makes sense on slide 27 (slide 3 note).
- Video is a placeholder. **Caption times are placeholders**, spread evenly over 40 s; replace with the SRT.

### 3 · q1 (slides 9–10) — input + applet
- Embedded applet: the flight-log elements are **dragged** to sort them from small to large (applet file from the content team: `שאלה 1 - מיון צילומי רחפנים.html`).
- Typed answers: range **30**, median **125**.
- Feedback state: the applet's numbers must show in the right order (110, 120, 125, 130, 140); "could be a picture and not the applet itself" (slide 10). Decide in phase 5.
- Check marks (a small ✓ gif) appear next to the two boxes in the feedback state.

### 4 · video-typo (slides 11–14)
- One video: slides 12–14. Slide 11 is the PLAY screen.
- Design note (slide 11): the designer tried to show their expressions but they came out not like the characters; use the first picture of them as the base.
- Video and caption times are placeholders.

### 5 · q2 (slides 15–16) — single choice
- Correct: option 3 ("הם טועים – התיקון ל-145 שינה את סדר הנתונים…").
- A picture of the corrected log (120 crossed out → 145) sits beside the stem. It needs **alt text** for accessibility (slide 15). Text not supplied: open question 5.

### 6 · q3 (slides 17–18) — single choice + applet
- Applet "the one meant for question 4, with the 145 correction" (slide 17): file `שאלה 4 - מיון צילומי רחפנים.html`. Elements are dragged.
- Feedback state: show the right arrangement; "can be a picture" (slide 18).
- Correct: "נכונה".

### 7 · next-test (slide 19) — explanation only

### 8 · q4 (slides 20–21) — single choice
- Correct: "לא נכונה". Lihi's picture beside the stem.

### 9 · q5 (slides 22–23) — typed answer 142
- The feedback holds an equation: `(650+x)/6 = 132 / ·6`, `650 + x = 792 / -650`, `x = 142`. Built with a live fraction. Check against the slide picture in phase 4.

### 10 · test-six (slide 24) — explanation
- Subtle animation that shows what the drone films. Automatic, loops, no controls.
- The design (PSD frame 24) still says **167** in the HUD text where the storyboard says **142** — designer to fix (see `PROGRESS.md`).

### 11 · q6 (slides 25–26) — drag to rows
- An **endless stack** of cards ("גדל", "קטן", "נשאר ללא שינוי"): after dragging one, another like it is behind it (slide 25). Built as four copies of each card in the bank; phase 4 makes them look like stacks.
- Key: השכיח → נשאר ללא שינוי; הממוצע → קטן; החציון → נשאר ללא שינוי; הטווח → גדל.
- The design (PSD frame 25) shows the older version of this question (one drop target, four buttons, "רק 12 תמונות"); the layout changes to the storyboard's.

### 12 · park-lights (slide 27)
- Subtle animation of the park lights twinkling a little. Loops.

### 13 · control-center (slide 28) — applet
- Applet `מרכז הבקרה.html`: clicking the computer screen makes it grow to full screen.
- **Continue only after the task is completed inside the applet.** The engine's gate counts seconds after start; it needs a "task completed" message from the applet instead. *To do (phase 5), via a HOOK, not the engine.* What completes the task: open question 7.

### 14 · party (slide 29)
- Animation (not a video): the young people gather for a photo, a flash with a sound like dim party music and a camera click; then a phone rises and the photo becomes a post on an unnamed social network; the likes go up fast.
- The post's text (name, "לפני 20 דקות", the message, "128") is live HTML in `.post-card`; confirm in phase 2 against the PSD.
- Built as CSS + a small hook: the young people slide in from both sides and gather; a flash and a camera click; dim party music (drawn in code); the phone rises; the photo flies into the post; the likes count up to 128. Alt text is a hidden description paragraph on the screen ("אנימציה: …"). The kids are the group photo split in two, not separate cut-outs: if they should really walk in one by one, the designer must supply them separately.

### 15 · q7 (slides 30–31) — single choice
- Correct: option 2 (the median).
- Feedback has "💡נקודה למחשבה" with two words highlighted (רוב הטיסות, החציון). Design note on slide 31: "עיצוב משוב" — the feedback box is bigger.
- Slide 30 has no "7." in the stem (open question 8).

### 16 · finish (slides 32–33)
- Animation (not a video): the drone flies over the park (loop), with the sound of the show in the background and the drone's sound above it. Sound only on the learner's click.
- "סיימתי" opens the final popup: **"כל הכבוד, המשימה הושלמה! / הציון שלך הוא __. / יש לסגור את המשימה בלחיצה על X."** The grade fills the blank; closing it with X ends the lomda and sends the score.

## Applets from the content team — check list (phase 5)
- The three files are Claude "bundled pages": they load React from `unpkg.com` and fonts from Google. They must be made **self-contained** (local libraries, local fonts) before they can go into `assets/app/`.
- Rename to ASCII names: `q1-sort.html`, `q3-sort.html`, `control-center.html`.
- They must post `APPLET_STARTED`; the control center must also report completion.
