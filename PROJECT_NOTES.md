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
- [ ] Add a favicon (the small icon in browser tabs) — need to create a small logo image first
- [x] Add `robots.txt` file — tells search engines how to crawl the site ✅
- [x] Add `sitemap.xml` file — helps Google find and index the site ✅
- [ ] Move original HEIC photo files out of the website folder to a separate backup location (they are excluded from GitHub but clutter the local folder)

### Lower Priority — Website Improvements
- [ ] Improve alt text on thumbnail images (currently "view 2", "view 3" etc. — more descriptive text helps Google Image search and accessibility)
- [ ] Add ARIA labels to Quick Look buttons for screen reader accessibility

### Future — Product Data Refactor (son's suggestion)
- [ ] Create a `products.json` file storing all product data: name, category, description, photos (main + thumbnails), date added, glow-in-the-dark flag, availability status
- [ ] Write a build script (`build.py` or `build.js`) that reads `products.json` and rewrites the product sections of `index.html` automatically
- [ ] After that: adding/removing products only requires editing the JSON file and running the script — no touching HTML directly
- [ ] Consider adding price field to JSON now even if prices aren't shown yet, so the data is ready when selling begins

### Business
- [x] Update website Contact section with real email address (hello@werecured.ca) ✅
- [ ] Decide on online selling method (Etsy, website shop, Instagram, etc.)
- [ ] Add prices to product listings when ready
- [ ] Write a privacy policy (required under Canadian law PIPEDA once selling begins)
- [ ] Write a return/shipping policy (customers expect this before purchasing)

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

## Accounts Summary

| Service | Purpose | Login | Password |
|---|---|---|---|
| Namecheap | Domain registration | knitwit1@telus.net | Dashlane |
| Google Workspace | Business email | janethardy@werecured.ca | Dashlane |
| GitHub | Website hosting (GitHub Pages) | janetlhardy / knitwit1@telus.net | Dashlane |
