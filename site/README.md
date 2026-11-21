# MERI walkthrough

Scroll-driven video walkthrough of the MERI studio: arrival, front desk, hallway,
cold plunge and sauna, back to the front desk, left through the glass door into the yoga room, back out and through the white door into the Pilates (Sculptformer) room, then back to the start with a booking call to action.

- `index.html`: the standalone page. Open it from any static host (`python3 -m http.server`).
- `artifact.html`: the same page as a fragment, used for the Claude artifact preview.
  Keep it in sync with `index.html`.
- `assets/tour.mp4`: the four shots joined, 1920x1080, keyframe every 6 frames for scrubbing.
- `assets/tour2.mp4`: the second video: front desk to the yoga entrance, through the glass door into the yoga room, and the white door into the Pilates room (366 frames, three stretches). Its first frame matches the tour at the front desk, so the page hands over between the two videos without a visible jump.
- `assets/box.mp4`: front desk, camera in to the box, lid opens (1080p, 5s). Played fast from the Memberships icon on the front desk; the three membership cards (`assets/m1-ritual.webp`, `m2-balance.webp`, `m3-rhythm.webp`) rise out of the open box. Closing plays it in reverse.
- `assets/ic-stone.png`, `ic-fire.png`, `ic-water.png`: the three room icons (cream on transparent). On the front desk, the stone icon opens the Yoga and Reformer journey and the fire and water icon opens Sauna and Cold plunge. Each click plays the footage at a fixed speed (`JRATE` in the script) and stops in the room, with a Back button that plays it in reverse.
- `assets/idle.mp4`: looping idle motion behind the intro blur.
- `assets/logo.png`, `assets/poster.jpg`.

Placeholders still to replace: stop titles and lines, the booking link behind "Book a session".
