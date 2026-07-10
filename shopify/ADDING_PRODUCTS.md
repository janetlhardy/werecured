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
7. **Collections** — add the product to the matching section collection:
   **Pendants · Earrings · Coasters · Bowls & Platters · Decorative Accents.**
   (This decides which section it shows up in, and the collection's order controls its position.)
8. **Glow-in-the-dark?** Add the tag **`Glow in the dark`** to show the little glow badge.
9. **Sales channels / Publishing** — make it available on the **Headless** channel (that's your website).
10. **Status = Active → Save.**
11. Refresh werecured.ca — it's there. To move it up/down in its section, drag it in the collection.

---

## If a product doesn't appear on the site, check:
- ✅ Status is **Active** (not Draft)
- ✅ It has a **price**
- ✅ It's available on the **Headless** channel
- ✅ It's in one of the five **Collections**

---

## One-time setup (do once, before launch)
1. Create **5 collections** named exactly: **Pendants, Earrings, Coasters, Bowls & Platters,
   Decorative Accents.**
2. Put the existing products into them quickly: **Products** list → filter by **Tag** (e.g., "Coasters")
   → select all → **Add to collection** → pick the matching collection. Repeat for each of the five tags:
   `Pendants`, `Earrings`, `Coasters`, `Bowls & Platters`, `Decorative Accents`.
3. Set prices, Quantity = 1, and publish everything to the **Headless** channel.
4. Tell Claude when this is done — Claude builds the Path A site rendering and you test locally.

---

## Want Claude to add a product for you instead?
Claude *can* add products to Shopify via the Admin API, but you'd still have to send the photos and
details — so using the **Add product** screen yourself is usually simpler. Claude is most useful for
**pricing**, **bulk changes**, and **fixing/rearranging** things. Just ask.
