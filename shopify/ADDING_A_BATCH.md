# Adding a batch of new pieces

When you've got a pile of new work photographed and want it all in the shop at once. For a single
piece it's quicker to just do it by hand — see `ADDING_PRODUCTS.md`.

_This file is kept off the public website._

---

## How it works

You and Claude split the job:

- **Claude** looks at your photos, suggests names and descriptions, checks them with you, tidies the
  photos up, and builds a spreadsheet (a "CSV") with all the details.
- **You** upload that spreadsheet to Shopify, then drag each piece's photos onto it.

The photos go **straight into Shopify**. They don't go into the website folder — see
[Why photos don't go in the website folder](#why-photos-dont-go-in-the-website-folder) at the bottom
if you're curious.

---

## Your part, step by step

### 1. Send Claude the photos

All of them, however you like. Claude can see them and work out which shots belong to which piece.

Helpful but not essential: mention anything that isn't obvious from a photo — if a piece glows in the
dark, what a bowl's made of, roughly how big something is.

### 2. Agree the names and descriptions

Claude will come back with a suggested name and description for each piece. **Have a read and change
whatever you like** — they're your pieces, and Claude is guessing from photos. This is the point to
say "that's not a bowl, it's a tray" or "I'd rather call that one Sea Glass".

Claude also needs a **price** for each. Either give one, or give the materials cost, roughly how many
hours it took, and how fiddly it was, and Claude will work it out using `PRICING_SCHEME.md`.

### 3. Claude sends you back two things

- **A folder of photos**, sorted into **one sub-folder per piece**, named after the piece. The photos
  inside are numbered — `…-1`, `…-2` and so on — and **number 1 is the one that'll show as the main
  photo**.
- **A CSV file** with all the names, descriptions, prices and settings.

### 4. Upload the CSV to Shopify

1. In Shopify admin, go to **Products**.
2. Click **Import** (top of the page).
3. Choose the CSV file Claude sent, then **Upload and continue**.
4. Shopify shows you a preview — have a quick look, then **Import products**.

Your new pieces are now in the shop, **but without photos yet**. That's expected.

### 5. Add the photos — one piece at a time

For each new piece:

1. Open the product in Shopify (**Products**, then click its name).
2. Find the **Media** box.
3. Open that piece's folder on your Mac, **select all the photos in it, and drag them onto the Media
   box.** They'll upload together.
4. Check the **first photo** is the one you want as the main image. If not, drag the thumbnails into
   a different order — the first one is what shows on the website.
5. **Save.**

Then on to the next piece. About a dozen pieces takes five or ten minutes.

> 💡 A whole folder can be dragged in at once, and 20–30 photos at a time is fine. If you've got a
> piece with a lot of shots, just do it in two goes.

### 6. Check they've all arrived

Refresh **werecured.ca** and look at the sections your new pieces should be in.

⚠️ **This is the step worth not skipping.** A piece with no photo **doesn't appear on the website at
all** — it doesn't show up broken or half-finished, it's simply not there, and nothing warns you. So
if a piece is missing, the first thing to check is whether its photos actually saved.

If something's still missing after that, ask Claude — Claude can read the live shop data and tell you
exactly which piece is off and why.

---

## If a piece doesn't show up

Check these, in this order:

- ✅ **Does it have photos?** Much the most common cause with this method.
- ✅ **Is the Product type exactly right?** It must be one of `Pendant`, `Earrings`, `Coasters`,
  `Bowls and Platters`, `Home Decor` — spelling and capitals matter. Claude sets this in the CSV, but
  it's worth knowing. (Full explanation in `ADDING_PRODUCTS.md`.)
- ✅ **Is it published to the Headless channel?** That's the one that feeds werecured.ca.
- ✅ **Does it have a price?**
- ✅ **Is the status Active**, not Draft?

---

## Why photos don't go in the website folder

We used to do this differently: Claude put the photos on the website, and the CSV had links so
Shopify could fetch them during the import. It worked, but it meant the website folder was carrying
**703 MB of photographs** that the site never actually showed — just so Shopify could grab a copy
once. GitHub Pages, which hosts the site for free, has a size limit of about 1 GB, so it was heading
for a wall.

Shopify keeps its own copy of every photo anyway. So now the photos go straight there, and the
website folder stays small.

The trade is the drag-and-drop step in stage 5 — a few minutes per batch, in exchange for never
worrying about the limit.

---

## Notes for Claude

- Compress photos at intake with **`sips -Z 2048 -s formatOptions 75`** before handing them over.
  2048 px is Shopify's threshold for zoom quality, so don't go below it for product shots. (The
  1500 px figure in `CLAUDE.md` predates the shop and is too small for product photos now.)
- Save them **outside the repository**, one sub-folder per product, files named
  `<product-handle>-1.jpeg`, `-2`, and so on. The intended main shot is `-1`.
- Avoid filenames ending in `_thumb`, `_small`, `_medium`, `large`, `grande`, `compact`, `icon` or
  `pico` — Shopify's CDN reads those as resizing instructions.
- Generate the CSV with **no `Image Src`, `Image Position` or `Image Alt Text` columns.** Only
  `Title` is genuinely required by Shopify (plus `Handle` where there are variant rows), so a CSV
  without image columns imports cleanly.
- Do **not** try to predict Shopify Files CDN URLs to put in the CSV. The URL pattern is stable, but
  Shopify appends a suffix when a filename collides and alters names ending in digits — which this
  naming convention uses. A silently renamed file means a silently missing photo. This was
  considered and rejected; see `docs/PROJECT_MEMORY.md`.
- After Janet reports she's done, offer to check the live storefront for products missing a photo or
  carrying an unrecognised Product type.

---

## Checking a batch went in properly (for Claude)

After Janet reports she's done, verify against the live storefront rather than trusting admin:

```
curl -s -X POST "https://fbkwka-jw.myshopify.com/api/2024-10/graphql.json" \
 -H "X-Shopify-Storefront-Access-Token: 4b5f552cdecea53a71057cf281cdd532" \
 -H "Content-Type: application/json" \
 -d '{"query":"{ products(first:20, query:\"<search>\") { edges { node { title handle productType availableForSale images(first:50){edges{node{url}}} priceRange{minVariantPrice{amount}} } } } }"}'
```

Check each product for: right `productType`, a price, at least one image, and
**`availableForSale: true`**.

⚠️ **`availableForSale: false` is the one that bites.** In August 2026 a product imported with
quantity 0 and showed as sold out on the live site while looking completely correct in the Shopify
admin. The fix is Products → the product → Inventory → Quantity → 1 → Save. A CSV can carry
`Variant Inventory Qty` and still land at zero, so always check this after an import.

Image filenames come back with a UUID suffix (`name-1_a3f8….jpg`) where the name collided with an
existing file — that suffix marks the **newly uploaded** copy, which is a handy way to tell new
photos from ones already on the product.
