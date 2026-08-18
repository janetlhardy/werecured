# What's in progress right now

Short-lived notes only. **Delete entries when they're done** — this file is only useful if it's
short and true. Anything that turns out to be a lasting decision belongs in `PROJECT_MEMORY.md`
instead.

_Updated: 2026-08-17._

---

## Waiting on Janet

### Moving the product photos out of the repository

The new photo pipeline is documented and in force for future batches, but the **existing ~1,053
product photos are still in `images/`**. They've done their job — every imported product's images
now live on Shopify's servers — so they can move to a local archive folder alongside
`werecured-HEIC-originals`.

- **Keep in `images/`:** the 9 the website actually uses — `IMG_4625` (About photo), `IMG_3064`
  (social share), and `IMG_3061`, `IMG_3091`, `IMG_3131`, `IMG_3134`, `IMG_3188`, `IMG_3309`,
  `IMG_3320` (source art for the print designs).
- **Effect:** published site drops from about 703 MB to roughly 5 MB.
- **Not a delete** — it's a move, and git history keeps every version regardless.
- **Side effect to accept:** the `werecured.ca/images/…` URLs inside the old import CSVs stop
  resolving. Those CSVs are historical records already.

Janet asked to confirm immediately before this runs, since it's the only bulk file operation.

---

## Worth a look sometime

### `CLAUDE.md` has no backup

`/Users/knitwit1/website/CLAUDE.md` sits one folder up, deliberately — it holds the rules shared
between We're Cured! and Janet's second site, `theshiveringsheep`. That placement is right.

But it's in **no git repository at all**, so it has no version history and no backup. Worth sorting
out when the second site next gets attention. **Deferred at Janet's request** — she rarely updates
that site and nearly all work happens here.

### Things I couldn't confirm from the repo

Not blocking anything, just flagged so nobody assumes they were checked:

- **Whether any Shopify products are drafts or unpublished.** The public API only shows published
  ones, so 153 is the visible count, not necessarily the total. Janet's Shopify admin would say.
- **Whether "Enforce HTTPS" is ticked in GitHub Pages settings.** The site serves over HTTPS
  correctly, which strongly suggests yes, but the setting itself wasn't opened.
- **Whether the `hello@werecured.ca` delivery problem is fixed.** `PROJECT_NOTES.md` says Janet's son
  was helping with a DNS/DMARC issue. Nothing in the repo can confirm either way.

---

## Recently finished

_Nothing outstanding from the August 2026 documentation work — the rest of it landed and the details
that matter went into `PROJECT_MEMORY.md`._
