# How the website works

This describes the site as it actually is today, not as it's planned to be. If you change something
here, update this file in the same commit.

_Last verified against the live site: 2026-08-17._

---

## The short version

`index.html` is the entire website — HTML, CSS and JavaScript all in one file, about 1,200 lines.
It's served free by GitHub Pages at werecured.ca. There's no build step, no dependencies, no
framework and no tests. Deploying means pushing to `main`.

The products come from Shopify at page load. Nothing about a product lives in the code.

---

## The stack

| Part | What it is |
|---|---|
| The site | A single hand-written `index.html`, styles and scripts inline |
| Hosting | GitHub Pages, serving the `main` branch |
| Domain | `werecured.ca` via the `CNAME` file; `werecured.com` redirects to it from Namecheap |
| Page generator | Jekyll (GitHub Pages runs it automatically). Only used for the `exclude` list in `_config.yml` |
| Shop | Shopify **Storefront GraphQL API**, version `2025-07`, called from the visitor's browser |
| Fonts | Bungee, Righteous and Nunito, loaded from Google Fonts |
| Deploy | `git push` to `main`. That's the whole process. |

---

## How products get onto the page

This is the part worth understanding properly.

1. The five product sections in `index.html` contain **empty** `<div class="gallery">` containers.
2. On load, `loadProducts()` asks Shopify for every published product, 60 at a time, following the
   pages until there are none left.
3. `renderSections()` reads each product's **Product type** and looks it up in the `TYPE_TO_SECTION`
   map to decide which section it belongs to.
4. It builds a card for each — photo, extra thumbnails, name, price, and either an **Add to Cart**
   button or a **Sold** badge depending on availability.
5. `wireCard()` attaches the lightbox and the Quick Look pop-up to each card as it's built.
6. Within a section, products are sorted **alphabetically by title**.

### The Product type map

| Product type in Shopify | Section id | Heading shown |
|---|---|---|
| `Pendant` | `pendants` | Pendants |
| `Earrings` | `earrings` | Earrings |
| `Coasters` | `coasters` | Coasters |
| `Bowls and Platters` | `bowls` | Bowls & Platters |
| `Home Decor` | `accents` | **Decorative Accents** |

Note that last row: the Shopify type is `Home Decor`, but the heading on the site reads *Decorative
Accents*. They're deliberately different, and it catches people out.

### When a product doesn't appear

A product is **silently skipped** — no error anywhere — if any of these is true:

- Its Product type isn't one of the five exact strings above (a blank or a typo does it)
- It has no image
- It has no variant, so no price
- It isn't published to the **Headless** sales channel

Shopify **Collections have no effect** on the site. They're fine to use for Janet's own organising,
but the code ignores them entirely.

As of 2026-08-17 there were 153 products live: 32 pendants, 11 earrings, 85 coasters, 17 bowls and
platters, 8 decorative accents.

---

## The cart and checkout

Built on Shopify's Cart API, all client-side — no server involved, which is what lets it work on
GitHub Pages.

- The cart's id is kept in the browser under `localStorage['wc_cart']`, so a cart survives a refresh.
- Adding the first item creates the cart; after that lines are added to it.
- The **Checkout** button links to Shopify's own hosted checkout page.
- A free **cork pads** checkbox appears in the cart only when a coaster is in it. Ticking it writes
  a cart attribute so the order tells Janet to include them.

### The Shopify keys in `index.html`

Near the bottom you'll find:

```js
const SHOPIFY = { domain: '…myshopify.com', token: '…', version: '2025-07' };
```

That token is the **public Storefront API token**. It's meant to be public — every visitor's browser
sends it — and it's read-only for products and cart operations. **Don't try to hide it, move it to a
server, or rotate it.** Rotating it without updating this file takes the shop offline.

---

## Where images come from

Two separate things, easily confused:

- **Product photos** are served by Shopify from `cdn.shopify.com`. The site never reads the local
  `images/` folder for products.
- **The `images/` folder** holds only images the website itself displays — Janet's About photo and
  the social-sharing preview — plus a few used as source art by the print designs in
  `print-materials/`.

Product photos **do not belong in this repository**. See `shopify/ADDING_A_BATCH.md` for how new
photos actually get to Shopify.

---

## Other pieces

- **Lightbox and Quick Look** — click a card to open the full product view. Arrow keys, Escape, and
  swipe on touch screens all work.
- **SEO** — meta description, Open Graph tags for social sharing, `robots.txt`, `sitemap.xml`, and a
  branded `404.html`.
- **`_config.yml`** — the `exclude` list keeps working files off the *public website*:
  `PROJECT_NOTES.md`, `PRICING_SCHEME.md`, `AGENTS.md`, `docs/`, `shopify/`, `marketing/` and
  `print-materials/`. Worth knowing: **this only hides them from werecured.ca, not from GitHub.**
  The repository is public, so anything committed is readable by anyone.

---

## Working on it locally

`.claude/launch.json` defines a preview server called `site` (`python3 -m http.server 8000`). It's
gitignored, so it only exists on Janet's Mac.

The local copy talks to the **live** Shopify store, so the real products and a working cart show up
in local preview too.

### Checking a change worked

There are no automated tests, so this is done by looking:

1. Load the site and count the product cards — expect 153 unless products have been added or sold.
2. Open the cart drawer, and open a product's Quick Look.
3. Check the browser console for errors.
4. If styling changed, check it at phone width too.

Be honest about what this does and doesn't prove. It confirms the page renders and the shop responds;
it doesn't test checkout, and nothing here catches a subtle visual regression.
