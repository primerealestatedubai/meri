# MERI walkthrough

Scroll-driven video walkthrough of the MERI studio: arrival, front desk, hallway,
cold plunge and sauna, back to the front desk, left through the glass door into the yoga room, back out and through the white door into the Pilates (Sculptformer) room, then back to the start with a booking call to action.

- `index.html`: the standalone page. Open it from any static host (`python3 -m http.server`).
- `artifact.html`: the same page as a fragment, used for the Claude artifact preview.
  Keep it in sync with `index.html`.
- `assets/tour.mp4`: the four shots joined, 1920x1080, keyframe every 6 frames for scrubbing.
- `assets/tour2.mp4`: the second video: front desk to the yoga entrance, through the glass door into the yoga room, and the white door into the Pilates room (366 frames, three stretches). Its first frame matches the tour at the front desk, so the page hands over between the two videos without a visible jump.
- `assets/idle.mp4`: looping idle motion behind the intro blur.
- `assets/logo.png`, `assets/poster.jpg`.

Placeholders still to replace: stop titles and lines, the booking link behind "Book a session".
