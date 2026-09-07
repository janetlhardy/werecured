# What belongs in this folder

**Only images the website itself puts on screen.** That's a short list:

- `IMG_4625.jpeg` — Janet's photo in the About section
- `IMG_3064.jpeg` — the preview image shown when the site is shared on social media
- `IMG_3061`, `IMG_3091`, `IMG_3131`, `IMG_3134`, `IMG_3188`, `IMG_3309`, `IMG_3320` — source art
  used by the designs in `print-materials/`
- `banner-background.jpeg` — a 3600 × 1200 band cut from `IMG_4374`, one of the rainbow-pour
  coasters, photographed close-up on 2026-09-07. Used by the booth banner only, and deliberately
  a separate file from the whole-coaster photos: the cards want a whole piece, the banner wants a
  wide band. Chosen by scoring every 3:1 crop of ten photos — it is the widest band that keeps
  7:1 contrast behind the lettering (50 dpi across 6 feet), has the richest colour of the ten,
  and catches almost no table (0.04%). Specks healed out; EXIF orientation stripped and the
  rotation baked in

## Product photos don't go here

They live in **Shopify**, and the website loads them from Shopify's servers when someone visits.
Nothing in this folder is used to display a product.

If you're adding new pieces, see `shopify/ADDING_A_BATCH.md`. Photos go straight into Shopify and
never pass through this folder.

_This used to work differently — photos were published here so Shopify could fetch them during an
import, which left 703 MB sitting in the repository for no lasting reason. The background is in
`docs/PROJECT_MEMORY.md`._

## Adding a new website image

If the site itself needs a new image — a new About photo, say — compress it first, the same way as
the others:

```
sips -Z 2048 -s formatOptions 75 yourphoto.jpeg
```
