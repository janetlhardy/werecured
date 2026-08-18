# Start here — We're Cured!

This is the website for **We're Cured!**, Janet Hardy's handmade resin art business in Victoria, BC.
Live at **https://werecured.ca**.

If you're an AI session picking this up, read this file first. It's short on purpose. The deeper
detail lives in `docs/` — links at the bottom.

There's also a shared `CLAUDE.md` one folder up (`/Users/knitwit1/website/CLAUDE.md`) that covers
rules common to both of Janet's websites. This file only covers what's specific to We're Cured!

---

## The one thing most likely to trip you up

**The products aren't in the code.** `index.html` ships with empty galleries, and the browser fills
them in by asking Shopify for the product list when the page loads.

Each product lands in a section based on its Shopify **Product type**, matched against five exact
spellings:

| Product type in Shopify | Section on the site |
|---|---|
| `Pendant` | Pendants |
| `Earrings` | Earrings |
| `Coasters` | Coasters |
| `Bowls and Platters` | Bowls & Platters |
| `Home Decor` | **Decorative Accents** ← note the heading differs from the type |

If the Product type is anything else — or the product has no price, no photo, or isn't on the
**Headless** sales channel — the site **skips it silently**. No error, no warning, it just isn't
there. This is the number one reason a product "doesn't show up", so check it first.

---

## How to talk to Janet

Janet runs the business and has no coding experience — and she shouldn't need any. She'll describe
what she wants in everyday terms ("change the text on the home page", "the cart isn't working").
Your job is to work out the technical side yourself.

- **Explain things in plain language.** Skip the jargon, or explain it the first time you use it.
- **Use Canadian English** — colour, jewellery, organised.
- **Don't ask her technical questions you can answer by looking.** Which file, which function, what
  the framework is — that's yours to find out. Ask her only about genuine business or product
  choices, like what to name a piece or what to charge.
- **Anticipate the confusing bits** rather than waiting for her to hit them.
- **Be warm and encouraging, but straight.** If something's broken or you're unsure, say so plainly.
  Don't over-reassure, and don't claim you've verified something you haven't.

The guides in `shopify/` and `marketing/` are written in the voice to match. If you're adding
documentation, write it like those.

---

## Git: just do it

**Commit and push as part of finishing a job — don't ask.** Janet doesn't use git and can't judge
when a commit is due, so asking either stalls things or leaves work stranded where it never reaches
the live site.

Finish every task the same way: **make the change → verify it → commit → push → explain in plain
English what changed and that it's live.**

Two things to keep in mind:

- **Pushing publishes.** GitHub Pages rebuilds from `main`, usually live within a minute or two.
  There's no staging step, so verify *before* you push.
- **This repository is public.** Never put a password, recovery code, API secret, or customer detail
  in any file here. (`shopify/shopify_recovery_codes.txt` sits on Janet's Mac and is correctly
  gitignored — leave it that way.)

Still stop and ask before anything hard to undo: `git reset --hard`, `git clean -fd`, force pushes,
rewriting history, deleting files, or overwriting a lot of files at once.

Work directly on `main`. Branches and pull requests would add process for no benefit here.

---

## Running and checking the site

There's no build step, no dependencies, nothing to install. `index.html` *is* the website.

To preview locally, `.claude/launch.json` defines a `site` server (`python3 -m http.server 8000`).
Note the local copy still pulls products from the **live** Shopify store, so the shop works locally
too.

**After changing `index.html`, check it actually works** — don't just assume it compiled:

1. Load the site and confirm the products render (there were **153** as of 2026-08-17).
2. Open the cart, and open a product's Quick Look.
3. Check the browser console is clean.

---

## Adding products

Janet does this in Shopify, not in the code.

- **One new piece:** `shopify/ADDING_PRODUCTS.md`
- **A whole batch:** `shopify/ADDING_A_BATCH.md` — Claude names and describes the pieces from the
  photos, builds an import CSV, and Janet adds the photos in Shopify. **Product photos don't go in
  this repository** — only images the website itself displays belong in `images/`.

---

## Where the rest of it lives

| File | What's in it |
|---|---|
| `docs/ARCHITECTURE.md` | How the site actually works — the Shopify render, the cart, deployment |
| `docs/PROJECT_MEMORY.md` | Decisions worth not reversing, and approaches already tried and dropped |
| `docs/CURRENT_STATE.md` | What's in progress or unresolved right now |
| `PROJECT_NOTES.md` | Janet's own business reference — accounts, domains, tax, to-dos |
| `PRICING_SCHEME.md` | How to price a piece. Use it every time. |
| `shopify/` | Plain-language guides for running the shop |

**Keep these honest.** If you change how the site works, update `docs/ARCHITECTURE.md` in the same
commit. If you make a real decision, record why in `docs/PROJECT_MEMORY.md`. If you finish something
in `docs/CURRENT_STATE.md`, delete the entry. And if you find that something written here contradicts
the actual code — **fix what's written**, don't work around it. Out-of-date notes are worse than no
notes, because they get believed.

Small edits — fixing a typo, swapping a photo, adding a product — don't need a documentation update.
