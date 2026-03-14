# We're Cured! — Project Notes

## Business Overview
- **Business name:** We're Cured!
- **Products:** Handmade resin jewelry (pendants, earrings) and home goods (coasters, home decor)
- **Physical location:** None currently — fully online
- **Selling channels:** To be decided

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

- [ ] Create GitHub account
- [ ] Create GitHub repository
- [ ] Push website to GitHub
- [ ] Enable GitHub Pages on the repository
- [ ] Connect `werecured.ca` domain to GitHub Pages (add CNAME file + update Namecheap DNS)
- [ ] Confirm `werecured.com` redirect to `werecured.ca` still works
- [ ] Add `werecured.com` to Google Workspace
- [ ] Add DNS records for `werecured.com` email in Namecheap
- [ ] Update website Contact section with real email address (janethardy@werecured.ca)
- [ ] Decide on online selling method (Etsy, website shop, Instagram, etc.)
- [ ] Add prices to product listings when ready

---

## Accounts Summary

| Service | Purpose | Login | Password |
|---|---|---|---|
| Namecheap | Domain registration | knitwit1@telus.net | Dashlane |
| Google Workspace | Business email | janethardy@werecured.ca | Dashlane |
| GitHub | Website hosting (GitHub Pages) | janetlhardy / knitwit1@telus.net | Dashlane |
