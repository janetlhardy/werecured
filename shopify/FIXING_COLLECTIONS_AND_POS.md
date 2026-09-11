# Why pieces are missing from Collections and from POS

_Found 2026-09-11. This file is kept off the public website._

Two separate problems with one thing in common: **both are about Shopify's own organisation, not
about your products.** Nothing is broken, and werecured.ca is completely unaffected.

---

## First, the reassuring bit

**Your website doesn't use collections at all.** It reads each product's **Product type** directly
and sorts it into the right section. That's why every piece shows up on werecured.ca even though
Shopify's own browse and the POS app are missing most of them.

So this is not urgent for the website. It **is** urgent for **November**, because the POS app is
what you'll be selling from at the show.

---

## Problem 1 — the collections were never kept up

Five collections were made early on and filled in **by hand**. Every batch imported since went into
**no collection at all**, because the import file has no collection column. They've drifted apart
ever since:

| Collection | In it | Should be | Missing |
|---|---|---|---|
| Pendants | 2 | 32 | **30** |
| Earrings | 0 | 11 | **11** |
| Coasters | 37 | 89 | **52** |
| Bowls & Platters | 10 | 26 | **16** |
| Decorative Accents | 6 | 18 | **12** |
| | | | **121 missing** |

That empty Earrings collection is exactly why the Earrings tile in POS shows nothing.

### The fix: make the collections fill themselves

Don't add 121 products by hand — they'd only drift again with the next batch. Make the collections
**automated**, so Shopify keeps them in step forever, including for pieces you haven't made yet.

⚠️ **Shopify won't let you convert an existing manual collection to an automated one.** You have to
make a new one alongside it. So, for each of the five:

1. **Products → Collections → Create collection**
2. Name it — use a temporary name for now, e.g. `Coasters (auto)`
3. Under **Collection type**, choose **Smart / Automated**
4. Set the condition: **Product type** — **is equal to** — and type the product type **exactly**:
   `Pendant`, `Earrings`, `Coasters`, `Bowls and Platters`, `Home Decor`
   (Note the singular **Pendant**, and **Home Decor** for Decorative Accents.)
5. **Save**, then check the product count looks right against the table above.

Once all five are right:

6. Delete the five old hand-made collections.
7. Rename the new ones to the proper names (`Coasters`, `Earrings`, and so on).
8. **Repoint any POS tiles** at the new collections — see below.

> Deleting the old collections is safe. Nothing on werecured.ca links to them, and no customer-facing
> page depends on them. Do it after the new ones are working, not before.

### The one-off alternative

If you'd rather not rebuild them, you can bulk-fill the existing ones: **Products**, filter by
**Product type**, select all, **Add to collection**. Quicker today, but it won't maintain itself —
you'd have to remember after every single import. The automated version is worth the extra half hour.

---

## Problem 2 — products aren't published to the POS channel

Separate from collections, and the more important of the two. **A product only appears in the POS app
if it's published to the Point of Sale sales channel.** Being on the website channel isn't enough —
they're independent.

The pieces that came in by CSV import almost certainly aren't on it.

### The fix

**First check the channel actually exists.** Installing the POS app on your phone does *not* add
the Point of Sale channel to your store — they're separate steps, and it's easy to assume the app
did it. Look in the left sidebar of Shopify admin under **Sales channels**. If Point of Sale isn't
listed, click the **+** beside the heading and add it (also findable under
**Settings → Apps and sales channels**).

Then:

1. **Products** → tick the box at the top to **select all**
2. **More actions → Include in sales channel**
3. Pick **Point of Sale** from the list
4. Apply

> If **Point of Sale** doesn't appear in that list, the channel still hasn't been added — go back
> and do that first. The menu only ever offers channels your store already has.

Then open the POS app on your phone, pull to refresh, and search for a piece you know is new. If it
comes up, it's working.

### ⚠️ This has to be redone after every import

New products from a CSV don't join the POS channel on their own. So **after every batch import, do
this again.** It's also worth checking whether Shopify will do it for you automatically —
**Settings → Sales channels → Point of Sale** — some plans offer a "publish new products
automatically" option. If yours does, turn it on and the problem goes away for good.

---

## Do this before November

Both jobs, in this order:

- [ ] Publish everything to **Point of Sale** (Problem 2 — do this one first, it's the one that
      stops you taking money at the show)
- [ ] Rebuild the five collections as **automated** (Problem 1)
- [ ] Repoint the POS tiles at the new collections
- [ ] Open the POS app and check each tile actually shows pieces
- [ ] Ring up a practice sale, as `CRAFT_SHOW_POS.md` describes

**Don't leave the POS check to the morning of the show.** A tile that looks fine in admin and comes
up empty on the phone is exactly the kind of thing that only shows itself when you test on the
device you'll actually be using.
