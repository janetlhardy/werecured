# What's in this folder

Guides for running the We're Cured! Shopify shop, plus the CSV files from past product imports.

_None of this appears on the public website._

## The guides

| File | What it's for |
|---|---|
| `ADDING_PRODUCTS.md` | Adding **one** new piece by hand in Shopify |
| `ADDING_A_BATCH.md` | Adding a **batch** of new pieces — Claude names them and builds a CSV, Janet adds the photos |
| `SHIPPING_SETUP.md` | Shipping rates and how to actually post things |
| `STORE_POLICIES.md` | Refund and shipping policy text to paste into Shopify |
| `CRAFT_SHOW_POS.md` | Selling in person at markets with Shopify POS |
| `SHOPIFY_SETUP.md` | How the shop was originally set up — a record, nothing to do |

---

## About the `.csv` files

⚠️ **These are records of imports that already happened. They are not the master list of products.**

**Shopify is the master list.** If you want to know what's in the shop, look in Shopify — or ask
Claude, who can read the live product data straight from the website.

Please don't rebuild the catalogue from these files. Three reasons they'd lead you astray:

- **They don't match what's live.** There are 181 product handles across these files, but 153
  products in the shop. Some pieces were merged, renamed, or never imported.
- **`pendants-import.csv` is a duplicate.** All 32 of its products are already inside
  `products-import.csv`. It's not an extra 32 pieces.
- **`new-products-2026-07.csv` has Product types the website doesn't recognise** — `Coaster set`,
  `Planter` and `Tray`. Those were fixed inside Shopify after importing, so the live shop is fine,
  but re-importing this file as it stands would create 19 products that **silently never appear on
  werecured.ca**. (The website only understands `Pendant`, `Earrings`, `Coasters`,
  `Bowls and Platters` and `Home Decor` — see `ADDING_PRODUCTS.md`.)

### The image links in these files don't work anymore

The older CSVs have an `Image Src` column pointing at `https://werecured.ca/images/…`. That was the
old way of doing things: photos were published to the website so Shopify could fetch them during an
import.

**That's not how it works now.** Photos go straight into Shopify and never enter this repository —
see `ADDING_A_BATCH.md`. The photos those links point at have moved to a local archive folder, so
the URLs no longer resolve.

This doesn't affect the shop at all. Shopify made its own copy of every photo when it imported them,
and that's what customers see. It just means these files are purely a historical record now.
