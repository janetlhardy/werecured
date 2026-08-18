# Decisions worth knowing about

Things a future session couldn't easily work out from the code alone: why the site is built the way
it is, what's already been tried and dropped, and which bits are more fragile than they look.

This isn't a diary. Add things that will still matter in six months, and correct anything that turns
out to be wrong rather than leaving it to mislead someone.

---

## The site renders products from Shopify ("Path A")

**Decided July 2026, live 2026-07-10 (commit `adc754f`).**

Before this, every product was a hand-written HTML card. `index.html` was 2,175 lines and adding a
piece meant editing markup by hand. The migration deleted all of it — the file dropped to about
1,039 lines — and the browser now builds the galleries from Shopify at page load.

**Why it matters:** the single most repeated activity in this repository's history was *fixing
photos attached to the wrong product*. At least fifteen commits do nothing else. Moving products into
Shopify made that Shopify's job, and the problem stopped.

**Don't undo this.** Putting product data back in the repo would bring that maintenance burden back
with it.

---

## The `products.json` + build script idea was dropped

An earlier plan — suggested by Janet's son, and still listed as a "future" to-do in
`PROJECT_NOTES.md` for a while — was to keep products in a `products.json` file and write a build
script that rewrote the HTML from it.

It was a reasonable idea for the problem at the time. **The Shopify migration solved that same
problem better**, because Janet edits products in an interface built for it rather than in a JSON
file, and inventory and checkout come along for free.

**Don't build it.** If it comes up again, this is why it didn't happen.

---

## Sections come from Product type, never Collections

The site sorts products into sections purely on Shopify's **Product type** field, via the
`TYPE_TO_SECTION` map in `index.html`. Collections are ignored completely.

The documentation once said otherwise and was corrected in commit `a3f920d`. The code has always
worked this way.

**This is the most fragile thing in the whole setup.** A Product type that's blank or slightly
misspelled means the product doesn't appear on the site, and *nothing reports it* — not the browser
console, not Shopify. Same for a missing photo or price. When something's missing, check this first.

---

## The Storefront token is public on purpose

The Shopify token in `index.html` is a **Storefront API** token. It's designed to be published — the
visitor's browser has to send it — and it's read-only for products and cart operations. Shopify
refuses it for anything sensitive; it can't even read inventory counts.

**It isn't a leaked secret and doesn't need rotating.** Hiding it would require a backend this site
deliberately doesn't have, and rotating it without updating `index.html` would take the shop offline.

The Shopify **Admin** API is a different thing — that token *would* be a real secret, and there
isn't one in this project.

---

## The site stays as one file

`index.html` holds the HTML, CSS and JavaScript together. That's deliberate, not neglect.

With no build step, one file is genuinely simpler: nothing to bundle, nothing to keep in sync,
and deploying is just pushing. Splitting it would add regression risk to a working shop for no real
gain. The shared `CLAUDE.md` asks for it to stay this way.

Related: **no framework, no bundler, no npm, no linter, no test runner.** Zero dependencies is why
this site has needed no maintenance since July 2026.

---

## Product photos don't live in this repository

**Changed 2026-08-17.**

The original pipeline published photos to `werecured.ca/images/` so that Shopify could fetch them
during a CSV import. It worked, but it meant the repository carried **703 MB of photos** purely as a
delivery mechanism — against GitHub Pages' roughly 1 GB limit — for something Shopify only needed
once, since it keeps its own copy after import.

Now the CSV is generated with **no image columns at all** (only `Title` is actually required), and
Janet adds the photos in Shopify by dragging one folder per product onto its Media area. Full
workflow in `shopify/ADDING_A_BATCH.md`.

**Two things established while designing this, worth not re-discovering:**

- Shopify **Files** CDN URLs *are* predictable and work without the `?v=` cache-buster. But Shopify
  **appends a suffix when a filename collides**, and is documented as altering names that end in
  digits — which the `<product-name>-1.jpeg` convention does. So generating a CSV from predicted
  Files URLs is unsafe, and that approach was rejected.
- Filenames must not end in `_thumb`, `_small`, `_medium`, `large`, `grande`, `compact`, `icon` or
  `pico`. Shopify's CDN reads those as image-resizing instructions.

**The trade-off, stated honestly:** this adds a manual step for Janet. If she imports a batch but
doesn't add the photos, those products have **no image — and the site silently skips them.** Always
confirm the photos are attached before calling a batch finished.

---

## The import CSVs are history, not source of truth

`shopify/*.csv` are records of past imports. **Shopify is the source of truth** for products.

They hold 181 product handles between them against 153 products actually live, `pendants-import.csv`
is entirely duplicated inside `products-import.csv`, and `new-products-2026-07.csv` contains Product
types (`Coaster set`, `Planter`, `Tray`) that the site doesn't recognise — those were corrected
inside Shopify after importing.

**Never regenerate the catalogue from these files.** See `shopify/README.md`.

---

## No sales tax is being charged

**Decided 2026-07-15.** Janet operates as a BC **small seller** / federal **small supplier** and is
below both thresholds, so no tax is collected. Tax is off at the store level *and* per product.

**Watch the $10,000 BC PST threshold** — it's the lower of the two and the one that'll arrive first
($30,000 for GST). The full reasoning, and how to switch tax back on when the time comes, is in
`PROJECT_NOTES.md`.

---

## The repository is public

Confirmed, and Janet is happy with it. No passwords, keys or customer data have ever been committed —
that's been checked across the whole history, and her recovery codes are correctly gitignored.

It does mean `_config.yml`'s `exclude` list is often misread. **It hides files from the website, not
from GitHub.** `PROJECT_NOTES.md` returns a 404 on werecured.ca but is fully readable on github.com.
So: never commit a password, recovery code, API secret or customer detail here.
