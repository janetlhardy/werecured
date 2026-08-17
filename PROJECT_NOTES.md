# We're Cured! — Project Notes

## Business Overview
- **Business name:** We're Cured!
- **Products:** Handmade resin jewelry (pendants, earrings) and home goods (coasters, home decor)
- **Physical location:** None currently — fully online
- **Selling channels:** To be decided
- **Instagram:** @were_cured
- **Website email:** hello@werecured.ca

---

## Website

### Files
- **Location on computer:** `/Users/knitwit1/website/`
- **Main file:** `index.html` — this is the entire website (single file)
- **Photos:** All stored as `.jpg` files in the `images/` subfolder (converted from HEIC iPhone photos using the macOS `sips` command)

### Design
- **Fonts:** Bungee (titles), Righteous (headings/labels), Nunito (body text) — all from Google Fonts
- **Color palette:** Hot pink, electric blue, lime green, orange, purple, yellow on a dark purple-black background
- **Sections:** Pendants (18 items), Earrings (5 items), Coasters (20 sets), Home Decor (4 items), About, Contact

### Web Hosting
- **Service:** GitHub Pages (free)
- **Status:** Setting up
- **GitHub repository:** To be created
- **GitHub account:** janetlhardy (knitwit1@telus.net — password in Dashlane)
- **How it works:** Website files are stored in a GitHub repository and automatically served as a live website. To update the site, changes are pushed to GitHub via git.

### File Structure
```
website/
├── index.html        ← the entire website
├── images/           ← all product photos (.jpg)
├── PROJECT_NOTES.md  ← this file
├── CLAUDE.md         ← instructions for Claude
└── .gitignore        ← tells git which files to ignore
```

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
- [ ] Enable "Enforce HTTPS" in GitHub Pages settings (waiting for certificate — check back in an hour)
- [x] Confirm `werecured.com` redirect to `werecured.ca` still works ✅

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

### Future — Product Data Refactor (son's suggestion)
- [ ] Create a `products.json` file storing all product data: name, category, description, photos (main + thumbnails), date added, glow-in-the-dark flag, availability status
- [ ] Write a build script (`build.py` or `build.js`) that reads `products.json` and rewrites the product sections of `index.html` automatically
- [ ] After that: adding/removing products only requires editing the JSON file and running the script — no touching HTML directly
- [ ] Consider adding price field to JSON now even if prices aren't shown yet, so the data is ready when selling begins

### Business
- [x] Update website Contact section with real email address (hello@werecured.ca) ✅
- [x] Decide on online selling method ✅ → **Shopify** (headless: Shopify runs products/inventory/checkout + in-person POS; werecured.ca stays as the custom storefront). Setup steps in `shopify/SHOPIFY_SETUP.md`; integration plan approved.
- [ ] Add prices to product listings when ready — use the method in `PRICING_SCHEME.md`
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
- **Status (as of 2026-07-05):** ⏳ Shopify is requiring **identity-document verification** before
  payments can be set up. Payments (Shopify Payments) are **blocked until that's approved**.
- **Products:** `shopify/products-import.csv` is ready — 132 products, all as **Drafts**, quantity 1,
  **no prices yet** (set prices on import using `PRICING_SCHEME.md`).
- **Next steps:** (1) finish identity verification → (2) import the CSV → (3) set prices →
  (4) create a Storefront API token and send it to Claude → (5) Claude wires cart/checkout into the site.

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

## Marketing / Social Media

- **Instagram:** @were_cured — main channel for reaching new customers and driving traffic to werecured.ca.
- **Guide:** `marketing/INSTAGRAM_GUIDE.md` — plain-language starter kit (bio, weekly plan, Reel ideas,
  caption templates, copy-paste hashtag sets, First Week Checklist). Kept off the public site.
- **Strategy in a nutshell:** lean on **Reels** (process/pour/glow-reveal videos), post ~3×/week,
  always end with a call to action + link to werecured.ca. Consistency over perfection.

### To do — Marketing
- [ ] Update Instagram bio + put werecured.ca in the profile website field (see guide, section 1)
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
