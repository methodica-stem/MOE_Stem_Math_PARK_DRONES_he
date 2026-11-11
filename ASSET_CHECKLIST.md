# Asset checklist — pictures exported from the PSD

PSD: `stem_drones.psd` (in the lomda folder, never copied into the project).
Everything goes into `assets/images/`. Claude exports the rows with
`psd_export.py`, then ticks them (☐ → ✔) once `check_assets.py` agrees.

Frame numbers (`#3 31`) are the inventory's: `#3` is the 3rd group from the top
of the Layers panel, `31` its name (the designer named the frames by the
storyboard's slide number).

## Shared (once for the whole lomda)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|
| ☐ | `assets/images/bg-question.jpg` | `#15 9/רקע` | 0 | 0 | 1920 | 1080 | Recipe A; the background of all seven question screens is the same picture |
| ☐ | `assets/images/ui-btn-next.png` | `#3 31/חיצים/כפתור קדימה` | 25 | 936 | 103 | 103 | Recipe B [shadow] |
| ☐ | `assets/images/ui-btn-back.png` | `#3 31/חיצים/כפתור אחורה` | 1781 | 936 | 103 | 103 | Recipe B [shadow] |
| ☐ | `assets/images/ui-btn-round.png` | `#3 31/כפתור עזרה` | 54 | 30 | 120 | 120 | Recipe B; text layer left out [shadow] |
| ☐ | `assets/images/ui-btn-check.png` | `#3 31/צדקתי?` | 283 | 855 | 187 | 115 | Recipe B; text layer left out [shadow] |
| ☐ | `assets/images/ui-play.png` | `#14 11/play` | 786 | 422 | 428 | 436 | Recipe B |

## Screen 1 — intro (PSD frame #17 2)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|
| ☐ | `assets/images/intro-bg.jpg` | `#17 2/רקע` | 0 | 0 | 1920 | 1080 | Recipe A |
| ☐ | `assets/images/intro-lights.png` | `#17 2/אורות - לאנימציה` | 0 | 36 | 1920 | 1026 | Recipe B; the layer the lights animation is made from [trim]. Source only: the page uses the eight `intro-fx-*.png` files that `tools/split_intro_lights.py` makes from it (sky, stage, screens, cool, pink, warm1-3) |

## Screen 2 — video-test (PSD frame #16 3)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|
| ☐ | `assets/images/video-test-poster.jpg` | `#16 3` | 0 | 0 | 1920 | 1080 | Recipe A; banner, arrows and PLAY hidden (done with `--layer "#16 3" --hide "טקסט¦חיצים¦play"`, bars here stand for the pipe) |

## Screen 3 — q1 (PSD frame #15 9)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|

## Screen 4 — video-typo (PSD frame #14 11)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|
| ☐ | `assets/images/video-typo-poster.jpg` | `#14 11` | 0 | 0 | 1920 | 1080 | Recipe A; arrows and PLAY hidden (done with `--layer "#14 11" --hide "חיצים¦play"`) |

## Screen 5 — q2 (PSD frame #13 15)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|
| ☐ | `assets/images/q2-log.png` | `#13 15/יישומון/יישומון` | 160 | 185 | 720 | 737 | Recipe B — the corrected flight log (the word "טעות" is painted in: see ASSET_LOCALIZATION) |

## Screen 6 — q3 (PSD frame #12 17)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|

## Screen 7 — next-test (PSD frame #11 19)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|
| ☐ | `assets/images/next-test-bg.jpg` | `#11 19/רקע` | 0 | -2 | 1920 | 1084 | Recipe A |

## Screen 8 — q4 (PSD frame #10 20)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|
| ☐ | `assets/images/q4-lihi.png` | `#10 20/יישומון/ליהי - חושבת` | 560 | 424 | 484 | 634 | Recipe B |

## Screen 9 — q5 (PSD frame #9 22)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|
| ☐ | `assets/images/q5-drone.png` | `#9 22/יישומון/יישומון` | 150 | 265 | 690 | 460 | Recipe B |

## Screen 10 — test-six (PSD frame #8 24)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|
| ☐ | `assets/images/test-six-bg.jpg` | `#8 24/משרד ומסך` | 0 | 0 | 1920 | 1080 | Recipe A |
| ☐ | `assets/images/test-six-view.jpg` | `#8 24/צילום הרחפן - לאנימציה` | 118 | 20 | 1685 | 959 | Recipe B; what the drone films, animated |
| ☐ | `assets/images/test-six-hud.png` | `#8 24/ממשק הרחפן` | 120 | 22 | 1681 | 954 | Recipe B; the drone's screen interface (Hebrew painted in: see ASSET_LOCALIZATION) |

## Screen 11 — q6 (PSD frame #7 25)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|

## Screen 12 — park-lights (PSD frame #6 27)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|
| ☐ | `assets/images/park-lights-bg.jpg` | `#6 27/רקע` | 0 | 0 | 1920 | 1080 | Recipe A |
| ☐ | `assets/images/park-lights-lights.png` | `#6 27/אורות הפארק - לאנימציה` | 267 | 218 | 1634 | 483 | Recipe B; no longer used (replaced by the screen 12 clip) |
| ☐ | `assets/images/park-lights-erez.png` | `#6 27/ארז` | 0 | 187 | 850 | 893 | Recipe B |
| ☐ | `assets/images/park-lights-lihi.png` | `#6 27/ליהי` | 1067 | 353 | 698 | 727 | Recipe B |

## Screen 13 — control-center (PSD frame #5 28)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|
| ☐ | `assets/images/control-center-bg.jpg` | `#5 28/רקע` | 0 | 0 | 1920 | 1080 | Recipe A |
| ☐ | `assets/images/control-center-icons.png` | `#5 28/מסך - אייקונים` | 835 | 205 | 341 | 106 | Recipe B |

## Screen 14 — party (PSD frame #4 29)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|
| ☐ | `assets/images/party-bg.jpg` | `#4 29/רקע` | 0 | -181 | 1920 | 1442 | Recipe A [trim] |
| ☐ | `assets/images/party-phone.png` | `#4 29/פוסט בטלפון/טלפון - גוף` | 1215 | 236 | 410 | 840 | Recipe B |
| ☐ | `assets/images/party-phone-screen.png` | `#4 29/פוסט בטלפון/טלפון - מסך` | 1228 | 249 | 390 | 820 | Recipe B |
| ☐ | `assets/images/party-avatar.png` | `#4 29/פוסט בטלפון/ארז - תמונת פרופיל` | 1518 | 313 | 70 | 70 | Recipe B |
| ☐ | `assets/images/party-post.png` | `#4 29/פוסט בטלפון/תמונת הפוסט` | 1228 | 563 | 384 | 290 | Recipe B |

## Screen 15 — q7 (PSD frame #3 31)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|

## Screen 16 — finish (PSD frame #2 32)
| ✔ | file | PSD layer | x | y | w | h | how |
|---|---|---|---|---|---|---|---|
| ☐ | `assets/images/finish-bg.jpg` | `#2 32/רקע` | 0 | 0 | 1920 | 1080 | Recipe A |
| ☐ | `assets/images/finish-drone.png` | `#2 32/רחפן - לאנימציה` | 597 | 195 | 556 | 272 | Recipe B; flies over the park, animated |

## Rebuilt in code (deliberately NOT exported)
- The white question panel (`משטח שאלה`), the darkening layer (`הכהיה`), the progress pills, the banner (`טקסט`, with its gradient), the feedback boxes, the typed-answer fields, the answer rings, the drop zones and the cards of question 6: CSS.
- Every text layer, including the check-button label, the help label and the monitor texts on screen 13: live HTML.
- The applet pictures `יישומון` of question 1 and 3: the real applets replace them (phase 5).
- The monitor texts of screen 13 (`מסך - כותרת`, `מסך - טקסט`, `מסך - תגית`, `מסך - כפתור`): Hebrew painted in; rebuilt as HTML in the applet's start card.
