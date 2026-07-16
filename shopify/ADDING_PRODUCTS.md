# We're Cured! — Adding a New Product

Your everyday workflow once the site is live. With **Path A**, the website builds its product grid
directly from Shopify, so **you never touch the website code** — you just add the product in Shopify
and it appears on werecured.ca. Nothing lives in the HTML.

_This file is kept off the public website._

---

## Add a product (do it all in Shopify)

1. **Shopify admin → Products → Add product.**
2. **Title** — the product name as it will appear on the site (e.g., *Sunset Mandala Set of 4*).
3. **Description** *(optional)* — a sentence or two about the piece.
4. **Media** — upload your photos.
   - The **first photo is the main image** on the site.
   - The rest become the **extra thumbnails** in the pop-up image viewer.
   - Drag to reorder them.
5. **Pricing → Price** — set it using the method in `PRICING_SCHEME.md`.
   - 💡 You can ask Claude to price it for you — just give the **materials cost, active hours, and
     difficulty**, and Claude runs the formula.
6. **Inventory** — tick **Track quantity**, set **Quantity = 1** (one-of-a-kind, so it auto-marks
   "Sold" after it sells). Make sure **"Continue selling when out of stock" is OFF**.
7. **Product type** — ⭐ THIS is what decides which section the product shows up in on the site.
   You must type it **exactly** as one of these five values (spelling and capitals matter — no plurals,
   no "&", no extra words):
   - `Pendant`
   - `Earrings`
   - `Coasters`
   - `Bowls and Platters`
   - `Home Decor`

   ⚠️ If the Product type is blank or spelled differently (e.g. "Coaster set", "Planter", "Tray",
   "Pendants"), the site has no section for it and **silently skips the product** — even when it's
   Active, priced, and on the Headless channel. This is the #1 reason a product doesn't appear.
8. **Glow-in-the-dark?** Add the tag **`Glow in the dark`** to show the little glow badge.
9. **Sales channels / Publishing** — make it available on the **Headless** channel (that's your website).
   (The other boxes — Online store, Point of sale, Shop — are *different* storefronts and do **not**
   put the product on werecured.ca. Headless is the only one that feeds your site.)
10. **Status = Active → Save.**
11. Refresh werecured.ca — it's there. Within a section, products are ordered **alphabetically by title**.

> **Note:** Collections do *not* control what shows on the website — the site ignores them and sorts
> purely by **Product type**. You can still use collections in Shopify for your own organizing, but
> they have no effect on werecured.ca.

### Adding a whole batch at once (bulk edit tip)
When you import or edit many products together, set Product type in the **bulk editor**
(Products → select all → **Edit products** → add the **Product type** column). Type the value in the
first cell, then **copy it and paste down the *entire* column** — select every cell first, or some rows
get left blank (a blank Product type = product won't show). After saving, ask Claude to double-check;
Claude can read the live site data and tell you exactly which ones, if any, still have the wrong type.

---

## If a product doesn't appear on the site, check (in this order):
- ✅ **Product type** is exactly one of: `Pendant`, `Earrings`, `Coasters`, `Bowls and Platters`,
  `Home Decor` (this is the most common cause — a blank or misspelled type means no section)
- ✅ It's available on the **Headless** channel (not just Online store)
- ✅ It has a **price**
- ✅ It has at least one **photo**
- ✅ Status is **Active** (not Draft)

💡 Can't tell which products are missing without comparing lists by hand? Just ask Claude — Claude can
read the live product data straight from Shopify and name the exact products that are off.

---

## How the site decides sections (reference)
The website (`index.html`) reads products from Shopify's Headless channel and drops each one into a
section **based only on its Product type field**:

| Product type (exact) | Website section |
|---|---|
| `Pendant` | Pendants |
| `Earrings` | Earrings |
| `Coasters` | Coasters |
| `Bowls and Platters` | Bowls & Platters |
| `Home Decor` | Home Decor |

To display, a product also needs: a **price**, at least one **photo**, and to be published to the
**Headless** channel. Collections are not used by the site.

---

## Want Claude to add a product for you instead?
Claude *can* add products to Shopify via the Admin API, but you'd still have to send the photos and
details — so using the **Add product** screen yourself is usually simpler. Claude is most useful for
**pricing**, **bulk changes**, and **fixing/rearranging** things. Just ask.
