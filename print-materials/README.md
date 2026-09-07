# We're Cured! — Print Materials

Groovy, funky print designs that match the website (Bagel Fat One wordmark + Righteous + Nunito,
on the hot-pink / rainbow-on-dark palette). Every design uses a "bleed" edge so a professional
printer can trim it cleanly.

## What's in this folder

| File | What it is | Finished size | Order this as… |
|---|---|---|---|
| `business-cards.pdf` | 2 pages: front + back | 3.5 × 2 in | Standard business cards, **double-sided** |
| `stickers.pdf` | 3 designs (1 per page) | 3 in round | Round die-cut / kiss-cut stickers, 3 inch |
| `thankyou-cards.pdf` | 2 pages: front + inside | 5 × 7 in | Flat greeting/thank-you cards, **double-sided** |
| `wrapping-paper.pdf` | 1 page repeating pattern | 12 × 12 in tile | Wrapping paper / gift wrap (the dotty background repeats seamlessly) |
| `booth-banner.html` | Booth banner for the gift show | 72 × 24 in | Vinyl banner, 6ft × 2ft, hemmed with grommets |
| `table-sign.html` | Table sign with the QR code to the shop | 5 × 7 in | 5 × 7 flat card, or print at home on card stock |

The `.html` files are the editable source. The `.png` files are just quick previews to look at.

## How to order (online print service)

These are set up for services like **VistaPrint**, **Canva Print**, **Sticker Mule** (stickers),
or a local print shop. When you upload a PDF:

1. Pick the matching product and the **finished size** from the table above.
2. If asked, choose **double-sided** for business cards and thank-you cards.
3. If it mentions "bleed," the files already include it — just say **yes / keep bleed**.
4. For stickers, choose **die-cut** or **kiss-cut**, **circle**, **3 inch**. The faint dashed
   ring in the design shows where it will be cut — it does **not** print.

## Show pieces — banner and table sign

The banner and the table sign are a pair, and they split the job on purpose:

- **The banner** carries the name, big enough to read from across the hall. It has **no QR code** —
  hung behind your table it is too far away for a phone to focus on.
- **The table sign** carries the **QR code** to `werecured.ca`. It stands on the table in a cheap
  acrylic 5 × 7 photo holder, within arm's reach, which is the only place a QR actually works.

The banner is the Ocean Daisy coaster photo full-bleed behind the Bagel Fat One wordmark, so it
matches the business cards. For the table sign, print the **photo background** version — that is
the one that goes with it.

Two notes live in `booth-banner.html` itself as comments, in case the design is ever revisited:
why the photo is zoomed to 130% (a plain `cover` crop ran off the coaster onto the table at both
ends), and why the scrim over it is set where it is (readability behind the small print). To make
the banner sharper, just replace `images/IMG_3091.jpeg` with a bigger copy — the file needs no
other edits.

The QR codes are drawn as vector shapes right in the HTML, so they stay crisp at any size and
there is no image file to lose. They encode `https://werecured.ca` at the highest error-correction
level, so they still scan if a corner gets scuffed.

## Photos used

The rainbow tie-dye and shimmer close-ups come straight from your own pieces:
IMG_3064, IMG_3309, IMG_3134, IMG_3131, IMG_3188 (all in the `images/` folder).

## Want changes?

Tell Claude what to tweak (different photo, wording, colours, a folded card instead of flat,
matching gift tags, etc.) and the PDFs can be re-made.
