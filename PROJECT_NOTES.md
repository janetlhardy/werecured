# We're Cured! — Project Notes

## Business Overview
- **Business name:** We're Cured!
- **Products:** Handmade resin jewelry (pendants, earrings) and home goods (coasters, home decor)
- **Physical location:** None currently — fully online
- **Selling channels:** Online at werecured.ca (Shopify checkout) + in person at markets via Shopify POS
- **Instagram:** @were_cured
- **Website email:** hello@werecured.ca

---

## Website

### Files
- **Location on computer:** `/Users/knitwit1/website/werecured/`
- **Main file:** `index.html` — this is the entire website (single file)
- **Photos:** Product photos live in **Shopify**, not here. The `images/` folder holds only the few images the website itself displays. See `shopify/ADDING_A_BATCH.md`.

### Design
- **Fonts:** Bungee (titles), Righteous (headings/labels), Nunito (body text) — all from Google Fonts
- **Color palette:** Hot pink, electric blue, lime green, orange, purple, yellow on a dark purple-black background
- **Sections:** Pendants, Earrings, Coasters, Bowls & Platters, Decorative Accents, About, Contact — the products in each are pulled live from Shopify, so the counts change on their own (173 pieces as of 2026-08-25)

### Web Hosting
- **Service:** GitHub Pages (free)
- **Status:** ✅ Live at https://werecured.ca
- **GitHub repository:** https://github.com/janetlhardy/werecured (**public** — see note below)
- **GitHub account:** janetlhardy (knitwit1@telus.net — password in Dashlane)
- **How it works:** Website files are stored in a GitHub repository and automatically served as a live website. To update the site, changes are pushed to GitHub via git — usually live a minute or two later.
- ⚠️ **The repository is public.** `_config.yml` keeps this file off werecured.ca, but that only hides it from the *website* — it's still readable by anyone on github.com. Never put a password, recovery code or customer detail in this folder. (Passwords belong in Dashlane, which is where they are.)

### File Structure
```
werecured/
├── index.html        ← the entire website
├── AGENTS.md         ← start-here file for Claude
├── docs/             ← how the site works, decisions, current state
├── images/           ← only images the website itself displays
├── shopify/          ← guides for running the shop
├── marketing/        ← Instagram guides
├── print-materials/  ← business cards, stickers, gift wrap
├── PROJECT_NOTES.md  ← this file
├── PRICING_SCHEME.md ← how to price a piece
├── CNAME             ← points GitHub Pages at werecured.ca
├── _config.yml       ← keeps working files off the public site
└── .gitignore        ← tells git which files to ignore
```
_(`CLAUDE.md` lives one folder up, in `/Users/knitwit1/website/`, because it's shared with
The Shivering Sheep.)_

---

## Domain Names

- **Registrar:** Namecheap (namecheap.com)
- **Namecheap login email:** knitwit1@telus.net
- **Password:** Saved in Dashlane
- **Domains purchased:**
  - `werecured.com` — redirects to `https://werecured.ca` (redirect set up in Namecheap)
  - `werecured.ca` — primary domain

---

## Email

- **Service:** Google Workspace
- **Login email:** janethardy@werecured.ca
- **Password:** Saved in Dashlane
- **Domain connected:** `werecured.ca` ✅
- **Domain connected:** `werecured.com` ❌ Not yet added
- **DNS records added in Namecheap for werecured.ca:**
  - TXT record: host `google._domainkey` (for email authentication/DKIM)
  - MX record (for receiving email)

### To do — Email
- Add `werecured.com` to Google Workspace so email works for both domains
- This requires adding the same TXT and MX records in Namecheap under the `werecured.com` domain settings

---

## Outstanding To-Dos

### GitHub & Hosting
- [x] Create GitHub account ✅
- [x] Create GitHub repository ✅
- [x] Push website to GitHub ✅
- [x] Enable GitHub Pages on the repository ✅
- [x] Connect `werecured.ca` domain to GitHub Pages (CNAME file + Namecheap DNS) ✅
- [x] Enable "Enforce HTTPS" in GitHub Pages settings ✅ (the site serves over HTTPS correctly — if you ever want to double-check the setting itself, it's in the repo's Settings → Pages)
- [x] Confirm `werecured.com` redirect to `werecured.ca` still works ✅

### New Pieces — Thinker Statuettes (August 2026)
- [x] Set a price for each of the four thinker sets ✅ (2026-08-19)
- [x] Light box arrived and all four sets reshot ✅ (2026-08-24) — a big improvement on the
      outdoor shots
- [x] Backlit Garden Bloom reshoot ✅ (2026-08-24) — worked beautifully, 11 backlit shots now lead
- [x] Individual figure shots for **Gilded Lagoon** and **Liquid Metal** ✅ (2026-08-25)
      — **all four sets are now fully photographed and ready to import**
- [x] Import `shopify/new-thinkers-2026-08.csv` into Shopify ✅ (2026-08-25)
- [x] Photos added to all four ✅ — verified live: 13 / 13 / 7 / 20
- [x] Switched from Draft to Active ✅ — all four confirmed live and buyable
- [x] Photo replacements done for Amethyst Crystal Coasters, Blue Dahlia Coasters and the
      Golden Tide Trinket Dish ✅

Four sets of three seated "thinker" figures, all Product type **Home Decor**:

| Set | Handle | SKU | Price |
|---|---|---|---|
| Garden Bloom Thinkers — Set of 3 | `garden-bloom-thinkers` | WC-3820 | $109 |
| Liquid Metal Thinkers — Set of 3 | `liquid-metal-thinkers` | WC-3825 | $65 |
| Moonstone Thinkers — Set of 3 | `moonstone-thinkers` | WC-3830 | $65 |
| Gilded Lagoon Thinkers — Set of 3 | `gilded-lagoon-thinkers` | WC-3835 | $65 |

The Garden Bloom set is priced higher because it took roughly three times the active labour
(1.5 hr vs ~35 min) — materials were the same. See `PRICING_SCHEME.md`.

**Photos — all four sets complete:** Garden Bloom 13, Gilded Lagoon 20, Liquid Metal 13,
Moonstone 7. `batch-2026-08b/<handle>/` holds the shots to upload, numbered, `-1` first. Superseded shots are kept as backups in
`batch-2026-08b/outdoor-originals/` and `batch-2026-08b/lightbox-frontlit/` and aren't used.

**Photo replacements — done.** `reshoots-2026-08/` holds the light box photos that went onto
**Amethyst Crystal Coasters**, **Blue Dahlia Coasters** and the **Golden Tide Trinket Dish**.
A few of the older outdoor **macro close-ups were deliberately kept** — at that magnification the
background and harsh light don't show, and they reveal surface detail the light box shots don't.
`blue-dahlia-coasters-2` (in hand) is kept as the **scale** shot. Rule of thumb: whole-product
shots first, close-ups last.

⚠️ **Watch the stock quantity on CSV imports.** Garden Bloom imported at qty 0 and showed as sold
out on the live site despite looking perfect in admin. Always check `availableForSale` after an
import — see the storefront query in `shopify/ADDING_A_BATCH.md`.

The Moonstone set photographs best on a **black background** — it shows the iridescent ghost
pigment, which washes out to plain cream on white. A white group shot leads so the product grid
stays consistent, with the black singles at positions 3–5.

Translucent pieces (Garden Bloom especially) need **light coming through them from behind**, not
front lighting — that's what makes the flowers glow the way they do in person.

### New Pieces — Batch 2026-08c ✅ DONE (2026-08-25)

- [x] Import `shopify/new-products-2026-08c.csv` ✅
- [x] Drag photo folders from `werecured-product-photos/batch-2026-08c/` ✅
- [x] Stock quantity fixed on Wisteria Shell Bowl and Aurora Thinkers ✅
- [x] Switched from Draft to Active ✅ — all four verified live and buyable
- [x] Opal Wave Bowl raised $50 → $75 to match the two new bowls ✅

| Piece | Handle | SKU | Price | Photos |
|---|---|---|---|---|
| Sapphire Blossom Coasters — Set of 4 | `sapphire-blossom-coasters` | WC-3840 | $70 | 10 |
| Abalone Shell Bowl | `abalone-shell-bowl` | WC-3845 | $75 | 12 |
| Wisteria Shell Bowl | `wisteria-shell-bowl` | WC-3850 | $75 | 9 |
| Aurora Thinkers — Set of 3 | `aurora-thinkers` | WC-3855 | $65 | 24 |

Both bowls are from the same mould as the **Opal Wave Bowl** and are roughly 18 cm across. Opal
Wave was listed at $50; Janet is raising it to $75 so all three match.

The Aurora Thinkers have glitter bases and **ghost pigment** upper bodies, which look completely
different in shade, sunlight and the light box — the sunlit shots showing the opal rainbow effect
are included deliberately, and the description explains it.

Scale shots (bowl beside a tape measure) sit at **position 2** on both bowls.

### Email
- [ ] Add `werecured.com` to Google Workspace
- [ ] Add DNS records for `werecured.com` email in Namecheap
- [ ] Fix hello@werecured.ca delivery (DNS/DMARC issue — son helping with this)

### High Priority — Website Improvements
- [x] Add lazy loading to all images (`loading="lazy"` on all 617 img tags) ✅
- [x] Add meta description and Open Graph tags (in `index.html` head) ✅
- [x] Create a custom 404 page (`404.html`) — branded error page ✅

### Medium Priority — Website Improvements
- [x] Add a favicon — smiley emoji on a dark circle (`favicon.png`, `favicon-32.png`, `apple-touch-icon.png`) ✅ Easy to swap the emoji later on request.
- [x] Add `robots.txt` file — tells search engines how to crawl the site ✅
- [x] Add `sitemap.xml` file — helps Google find and index the site ✅
- [x] Move original HEIC photo files out of the website folder ✅ → now in `/Users/knitwit1/website/werecured-HEIC-originals` (49 photos + iPhone sidecar files)

### Lower Priority — Website Improvements
- [x] Add ARIA labels for screen readers ✅ (Quick Look buttons now name their product; lightbox close/prev/next buttons + dialog role labeled)
- [~] Improve alt text on thumbnail images — reviewed: the 231 "view N" thumbnails already include the product name (e.g., "Purple confetti pendant view 2"), which is reasonable for screen readers. Main product images have full descriptive alt text. Rewriting all 231 by hand risks inaccuracy without viewing each; leaving as-is unless we improve them gradually.

### ~~Future — Product Data Refactor (son's suggestion)~~ — no longer needed ✅

_This was a good idea for the problem at the time: keep all the product details in a `products.json`
file and write a build script that rewrites `index.html` from it, so adding a piece wouldn't mean
editing HTML by hand._

**The move to Shopify (July 2026) solved the same problem better** — products live in Shopify, the
website builds its galleries from them automatically, and inventory and checkout come along for
free. There's nothing left for a JSON file and build script to do, so **this isn't being built**.
Kept here so the idea doesn't get proposed again from scratch.

### Business
- [x] Update website Contact section with real email address (hello@werecured.ca) ✅
- [x] Decide on online selling method ✅ → **Shopify** (headless: Shopify runs products/inventory/checkout + in-person POS; werecured.ca stays as the custom storefront). Setup steps in `shopify/SHOPIFY_SETUP.md`; integration plan approved.
- [x] Add prices to product listings ✅ — all 153 pieces priced ($25–$150). Use `PRICING_SCHEME.md` for each new piece.
- [x] Write a privacy policy ✅ (Shopify template) — see `shopify/STORE_POLICIES.md`
- [x] Write a return/shipping policy ✅ (all-sales-final + damaged-refund; flat-rate shipping) — `shopify/STORE_POLICIES.md`
- [x] Turn OFF tax collection in Shopify ✅ (2026-07-15) — "Charge tax" unticked on all products (small seller — see Sales Tax section). Confirm via a test checkout showing $0 tax.
- [ ] Keep an eye on gross sales vs the **$10k BC PST** threshold (then $30k GST) — register when approaching

---

## Print & Packaging Materials

Print-ready designs live in the `print-materials/` folder (excluded from the public website).
They match the site branding, using a groovy retro wordmark font (**Bagel Fat One**) mixed with
Righteous and Nunito, on the rainbow-on-dark palette.

| File | What it is | Finished size |
|---|---|---|
| `business-cards.pdf` | Front + back | 3.5 × 2 in, double-sided |
| `stickers.pdf` | 3 designs | 3 in round die-cut |
| `thankyou-cards.pdf` | Front + inside | 5 × 7 in, double-sided |
| `wrapping-paper.pdf` | Repeating gift-wrap pattern | 12 × 12 in seamless tile |
| `gift-tags.pdf` | 9 "Thank You" tags per sheet | Letter cardstock (cut + punch at home) |

- All files include a print "bleed" edge, ready for an online service (VistaPrint, Canva Print,
  Sticker Mule) or a local print shop. See `print-materials/README.md` for ordering steps.
- Featured close-up photos: IMG_3064, IMG_3309, IMG_3134, IMG_3131, IMG_3188.
- Business card front: name centred on the bright **Ocean Daisy** coaster (IMG_3091); back is **plain white** with the rainbow logo.
- `business-card-coaster-options.html/.png` keeps the four coaster mock-ups that were considered.

### To do — Print materials
- [ ] Choose a print service and order a small test batch of business cards + stickers
- [ ] Decide on sticker cut type (die-cut vs kiss-cut) and quantity
- [x] Matching "Thank You" gift tags created (`gift-tags.pdf`) ✅

---

## Online Store (Shopify — headless)

Plan: **headless Shopify** — Shopify holds products, inventory, and checkout; werecured.ca stays
the custom storefront ("Enhance current cards" approach). In-person sales will use **Shopify POS**
so online + markets share one inventory. Full plain-language steps: `shopify/SHOPIFY_SETUP.md`.

- **Account:** created, signed in via the **Google account janethardy@werecured.ca**.
- **Status: ✅ Live since 2026-07-10.** Identity verification cleared, payments active, the website
  renders products straight from Shopify, and the cart and checkout work. **153 pieces live** as of
  2026-08-17, all priced and photographed.
- **Adding more:** one piece at a time → `shopify/ADDING_PRODUCTS.md`. A whole batch →
  `shopify/ADDING_A_BATCH.md`.

_The July 2026 setup steps (identity verification, the first CSV import, wiring up the cart) are all
finished. They're kept in `shopify/SHOPIFY_SETUP.md` as a record of how the shop was built._

### Sales Tax (BC) — currently charging NO tax

Janet lives in **BC** and operates as an unregistered **small seller / small supplier** (sole
proprietor, no business number, selling online from home + occasional markets). Under Canadian and
BC rules she is **not required to register for or charge any sales tax** while under the thresholds:

- **BC PST (7%):** exempt as a **"small seller"** while gross sales are **≤ $10,000** over the previous
  12 months **and** she has no established commercial premises (home + markets qualifies). This is the
  **lower threshold — the one to watch.**
- **GST (5%, federal):** exempt as a **"small supplier"** while total sales are **under $30,000**
  over a rolling 12 months.

**Decision (2026-07-15): charge no tax.** In Shopify, tax collection is being turned **off**:
- Settings → Taxes and duties → Canada: no GST/PST number entered, no tax collected.
- Per-product **"Charge tax on this item"** unticked. (Bulk-edit method: Products → select all →
  **Edit products** → add the **Charge tax** column → uncheck all → Save. New products: untick it on
  the product page before saving.)

⚠️ **Watch the $10k PST threshold.** Once gross sales approach $10,000 in any 12-month period, Janet
must register for BC PST and start charging 7% (and register for GST at $30,000). Use Shopify
Analytics to keep an eye on the running total. BC PST info line: **1-877-388-4440**.

### How to turn tax back ON later (when registering)

Two switches control tax: (1) the **store-level master switch** — Settings → Taxes and duties, where
you enter a GST/PST number and set a region to collect; and (2) the per-product **"Charge tax on this
item"** box. **Tax is only charged when BOTH are on.** Right now the master switch is off, so no tax is
charged regardless of the checkboxes; the per-product boxes were also unticked as a safety measure.

When gross sales hit the threshold and Janet registers:
1. **Master switch:** Settings → Taxes and duties → Canada → enter the **PST (and later GST) number**
   and set BC to collect. This is the main one.
2. **Re-tick the products in bulk** (not one-by-one): Products → select all → **Edit products** → add
   the **Charge tax** column → tick the first cell and copy it down the whole column → **Save**.
   (New products default to "Charge tax" already ticked, so only the previously-unticked ones need it.)
3. In **POS**, the same tax settings apply automatically once the master switch is on.

_Alternative lower-effort approach (not currently used): leave every product's "Charge tax" box ticked
and rely solely on the master switch being off. Then registering = flip the one master switch, no bulk
edit needed. Current setup unticks per-product instead, which is a touch safer._

_Note: general guidance, not accountant advice — confirm edge cases with the CRA / BC Ministry of Finance._

## In-Person Sales — Shopify POS (craft shows / markets)

In-person sales use the **Shopify Point of Sale (POS)** app, which shares one inventory with the
online store. POS sales live on the **Point of Sale** channel — completely separate from the
**Headless** channel that feeds werecured.ca, so nothing sold in person appears on the website.

### Taking card payments — Tap to Pay
- **Phone = the card reader.** Shopify **Tap to Pay** turns the phone itself into the reader; the
  customer taps their card/phone/watch on it. No separate device needed.
- **iPhone XS or newer** (recent iOS) supported; many newer **Android phones** too.
- **iPad/tablet can NOT be the tap reader** — it can run POS and ring up sales, but needs a separate
  card reader or manual card entry. **Use the phone for tap-to-pay.**
- **Manual card entry** (typing the number) works on either device as a backup.
- Card sales deposit to the **same Shopify Payments bank account** as online orders.

### One-time setup
- [ ] Download **Shopify Point of Sale** app (separate from the admin app) on the phone
- [ ] Sign in (janethardy@werecured.ca — Google sign-in; password in Dashlane)
- [ ] POS menu → **Settings → Payments → Set up Tap to Pay on iPhone** → accept terms
- [ ] Confirm **Shopify Payments** is active (same as online payments)
- [ ] Do a small **test sale + refund** to confirm it all works
- Note: **POS Lite is free/included** — no need for paid POS Pro for markets.

### Selling an in-person-only item (not on the website)
Two ways — neither touches werecured.ca:
1. **Quick custom sale (easiest for one-offs):** POS sale screen → **Add custom sale** → type a name
   + price → add to cart → checkout. Nothing gets added to the catalogue or website.
2. **POS-only product (if reselling / tracking stock):** create the product but publish it to the
   **Point of Sale** channel only — leave **Headless unchecked** so it stays off the website.

### Craft-show day checklist
- [ ] Phone charged + charging cable / battery bank
- [ ] Shopify POS app installed, signed in, Tap to Pay tested
- [ ] Internet available (wifi or cell data — required to take payment)
- [ ] Cash float for change (if taking cash); record cash sales in POS too
- [ ] Packaging: bags, thank-you cards, business cards, stickers
- [ ] Price list / prices visible on items

## Current focus (decided 2026-08-25)

**Uploading new pieces is paused.** With 173 products live the site has plenty of variety, and
nothing has sold online yet — but the cause is **reach, not stock**. The Instagram account
(@were_cured) is set up properly, bio and werecured.ca link in place, with posts up — but around
**59 followers** as of 2026-08-25. That's the bottleneck. Adding more products would not have
fixed it.

_Janet's daughter helps with Instagram._

So the plan is:
- **Keep the remaining inventory for the gift show, first weekend of November 2026.** Roughly 30–40
  pendants, no two alike, all around $50. Sell them via POS **Add custom sale** — no listings or
  photography needed (see the In-Person Sales section).
- **Photograph and list only what doesn't sell**, after the show.
- **Take one group photo of all the pendants before the show** — a strong pre-show Instagram post,
  a record of what was there, and insurance on ~$2,000 of stock.
- **Make sure every show customer leaves with the website address** — cards, stickers, a QR code on
  the table. Show buyers are the warmest possible audience for later online sales.

Note for pricing at the show: keep pendants at the online price (~$50) so nobody finds a different
price afterwards. A bundle (2 for $90, 3 for $130) moves stock and reduces what needs photographing
later.

## Marketing / Social Media

- **Instagram:** @were_cured — main channel for reaching new customers and driving traffic to werecured.ca.
- **Guide:** `marketing/INSTAGRAM_GUIDE.md` — plain-language starter kit (bio, weekly plan, Reel ideas,
  caption templates, copy-paste hashtag sets, First Week Checklist). Kept off the public site.
- **Strategy in a nutshell:** lean on **Reels** (process/pour/glow-reveal videos), post ~3×/week,
  always end with a call to action + link to werecured.ca. Consistency over perfection.

### To do — Marketing
- [x] Update Instagram bio + put werecured.ca in the profile website field ✅ (verified live 2026-08-25)
- [ ] Post first process/glow Reel and 2 finished-piece photos this week (First Week Checklist)
- [ ] Work through `marketing/FIRST_MONTH_POSTS.md` — 4 weeks of ready-to-paste captions for real pieces
- [ ] Claude can help: captions for specific pieces, a monthly posting calendar, fresh hashtag sets

## Accounts Summary

| Service | Purpose | Login | Password |
|---|---|---|---|
| Namecheap | Domain registration | knitwit1@telus.net | Dashlane |
| Google Workspace | Business email | janethardy@werecured.ca | Dashlane |
| GitHub | Website hosting (GitHub Pages) | janetlhardy / knitwit1@telus.net | Dashlane |
| Shopify | Online store + POS | janethardy@werecured.ca (Google sign-in) | via Google / Dashlane |
