# Marketing Class — daily educational series (approved by Safwan 25 Nov 2026)

One educational carousel per day, posted at 17:41 Dubai time, separate from the 3 fun posts.

## Fixed series look (do not change)
- **Cover (slide 1) is identical every lesson**: solid maroon #6B1E2E, cream "MARKETING CLASS" badge top-left, gold "LESSON" + huge gold lesson number (Playfair Display), outlined tag (platform/category), italic Playfair topic name, Arabic topic, one-line hook EN + Sudanese AR, photo **02-arms-crossed.jpg** in a gold-outlined arch bottom-right, cream footer strip "@safwanistaa · a new lesson every day · Swipe". Only the `COVER` fields change.
- Inner slides: cream #F6F1E7, maroon top bar, "MARKETING CLASS" badge + "LESSON NN · TOPIC", slide counter, gold kicker, Playfair Display headings, Inter body, IBM Plex Sans Arabic (Sudanese dialect) lines, footer "@safwanistaa · Save & share with a marketer".
- Last slide: "Learned something? Pass it on." + Save / Send / Follow for Lesson NN+1 + "What should Lesson NN+1 be?" box. No swipe cue; "Save for later" instead.
- 7–9 slides. Lesson structure: cover hook → what it is (simple) → steps → examples / message map → mistakes + fixes → screenshot-able checklist → CTA.

## How to build
`templates/marketing-class/build_lesson01.py` is the reference. Copy it to a scratch dir as build_lessonNN.py, change LESSON/TOPIC/N, the COVER dict and the inner slides, run it, copy assets/photos/02-arms-crossed.jpg into the slides dir as photo.jpg, render with tools/render_dc.py, and keep the script in posts/<folder>/src/.

## Content rules
- Teach ONE practical thing per lesson, beginner-to-intermediate, actionable, save/share-worthy.
- Only evergreen strategy, or platform facts verified in search that day. Avoid exact platform limits that change often unless verified today.
- No real brand logos; generic UI only.
- Workshop "مقدمة إلى عالم التسويق" (12 Dec 2026) may be mentioned on a lesson at most every few days, never after 12 Dec.
- Log every lesson in posts/LESSONS.md and never repeat a topic.
