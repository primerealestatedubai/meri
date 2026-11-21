# MERI walkthrough

Video walkthrough of the MERI studio. Scrolling takes the visitor from the arrival up the stairs to the front desk, and stops there. From the front desk, icons lead to the rest: the Memberships icon (box and cards), the stone icon (Yoga Studio and SculptFormer, with an icon on each door) and the fire and water icon (cold plunge and sauna, each with an icon that opens a photo gallery). The old full-length scroll (sauna, yoga, booking end screen) was cut from `STEPS`; the booking end screen is currently unreachable.

- `index.html`: the standalone page. Open it from any static host (`python3 -m http.server`).
- `artifact.html`: the same page as a fragment, used for the Claude artifact preview.
  Keep it in sync with `index.html`.
- `assets/tour.mp4`: the four shots joined, 1920x1080, keyframe every 6 frames for scrubbing.
- `assets/tour2.mp4`: the second video: front desk to the yoga entrance, through the glass door into the yoga room, and the white door into the Pilates room (366 frames, three stretches). Its first frame matches the tour at the front desk, so the page hands over between the two videos without a visible jump.
- `assets/box.mp4`: front desk, camera in to the box, lid opens (1080p, 5s). Played fast from the Memberships icon on the front desk; the three membership cards (`assets/m1-ritual.webp`, `m2-balance.webp`, `m3-rhythm.webp`) rise out of the open box. Closing plays it in reverse.
- `assets/ic-stone.png`, `ic-fire.png`, `ic-water.png`: the three room icons (cream on transparent). On the front desk, the stone icon opens the Yoga and Reformer journey and the fire and water icon opens Sauna and Cold plunge. Each click plays the footage at a fixed speed and stops in the room, with a Back button that plays it in reverse. `JRATE` (1.3x) is the default speed; the sauna and cold plunge run uses `HEATRATE` (3.9x). Inside the rooms the icons sit on the pools, the sauna door and the two doors (`SPOTPT` in the script).
- `assets/g-plunge-*.webp`, `g-sauna-1.webp`: placeholder photos for the two galleries (`GAL` in the script). Replace the files or edit the lists.
- `assets/idle.mp4`: looping idle motion behind the intro blur.
- `assets/logo.png`, `assets/poster.jpg`.

Placeholders still to replace: stop titles and lines, the booking link behind "Book a session".
