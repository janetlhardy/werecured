# We're Cured! — Shopify Setup Guide

Plain-language steps for connecting a **headless Shopify store** to the existing website.
"Headless" just means: Shopify holds your products, inventory, and checkout, while werecured.ca
stays as your custom storefront. Your in-person sales (Shopify POS) and online sales share **one
inventory**, so a piece sold at a market shows as "Sold" online automatically.

_This file is kept off the public website._

---

## 📍 Current status (2026-07-05)
- ✅ Shopify account **created** — signed in with the **Google account janethardy@werecured.ca**.
- ⏳ Shopify is asking for **identity-document verification** before payments. **Payments are on hold
  until that's approved** — so Step 2 below is blocked for now. Everything else can proceed.
- ✅ **`products-import.csv` is ready** in this folder (132 products, drafts, quantity 1, no prices yet).
- ▶️ **Next up:** finish verification, then do Step 3 (import) and Step 4 (prices).

---

## Your part — do these in order

### 1. Create the store
- Go to **shopify.com** → **Start free trial**. Pick the **Basic** plan when asked.
- Store name: **We're Cured!**
- Currency: **Canadian Dollar (CAD)**. Enter your business address.

### 2. Turn on payments
- **Settings → Payments** → activate **Shopify Payments** → enter your banking/deposit details.
- **Leave "Test mode" ON** for now, so Claude can test the website without real charges.
  Claude will tell you when to turn it off to go live.

### 3. Import your products (bulk)
- Claude gives you a file called **`products-import.csv`** (in this `shopify/` folder).
- In Shopify: **Products → Import → Add file** → choose `products-import.csv` → **Upload and continue** → **Import products**.
- Your photos load in automatically from the website links. Keep werecured.ca online during import.
- Products import as **Drafts** (hidden) so nothing goes live at $0 before you set prices.

### 4. Set prices (use `PRICING_SCHEME.md`)
- Open each product → set the **Price** using the pricing method → confirm **Quantity = 1** and
  **"Track quantity"** is on → set status to **Active** → **Save**.
- Tip: you can ask Claude to help price any piece — Claude will ask the few questions needed.
- (Shopify's bulk editor lets you set many prices on one screen: Products → select all → **Edit**.)

### 5. Get the website key (Storefront API token) — this is what links Shopify to your site
- **Settings → Apps and sales channels → Develop apps → Create an app** → name it **Website**.
- Open **Configuration → Storefront API** → **Configure** and tick:
  - read products,
  - read product inventory,
  - manage (read/write) carts & checkouts.
- **Save → Install app → API credentials** → copy the **Storefront API access token**.
- **Send Claude two things:** that **token** and your store address (looks like **yourshop.myshopify.com**).
- ✅ This token is **safe to share and to put on the website** — it can only *read* products and
  build shopping carts. It cannot see orders, customers, or money.

### 6. In-person selling (later, when you're ready for markets)
- Install the **Shopify POS** app on your phone/tablet and order a **Shopify card reader**.
- It uses the same inventory as the website — sell once, it's gone everywhere.

---

## After that — Claude's part
- Builds the "Add to Cart", live price, "Sold out", and cart/checkout into the website using your token.
- Tests a full pretend order in Shopify **test mode**.
- When it all works, you flip payments out of test mode and you're **live**.

---

## Adding a NEW product later (your future workflow)
For now (Phase 1):
1. **In Shopify:** Products → Add product → upload photos, type the name & description, set price,
   set Quantity = 1 → Save (Active).
2. **Tell Claude** the new product's name so a matching card is added to the website.
   (The website card and the Shopify product must share the **same name** so they link up.)

Later (Phase 2, optional): Claude can automate step 2 so new products appear on the site by
themselves — full self-serve.

---

## Good to know
- **One-of-a-kind:** every item is Quantity 1, so it auto-marks "Sold" after it sells (online or in person).
- **Your email and domain are unaffected** — we don't change your mail settings; werecured.ca stays on GitHub Pages.
- **Shipping:** later, set product weights in Shopify so it can calculate postage (resin is heavy!).
