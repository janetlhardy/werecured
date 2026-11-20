# Making Facebook & Instagram shop links land on werecured.ca

## Why this is needed

When someone taps a product in your Facebook or Instagram shop, Meta sends them to **Shopify's own
built-in shop** (at `fbkwka-jw.myshopify.com`), not to werecured.ca. Your pieces don't live in that
built-in shop. They're set up to show only on werecured.ca. So people were landing on
"page not found".

The fix is a short bit of code added to Shopify's built-in shop. It sends anyone who arrives there
straight on to werecured.ca, and if they tapped a particular piece, it opens that piece. It takes
about five minutes, and it's easy to take out again.

It doesn't touch checkout, orders, Point of Sale or your products.

---

## Steps (on the computer; this is much easier than on the phone)

1. Sign in to **Shopify admin**.
2. In the left-hand menu, click **Online Store** (under "Sales channels"). It opens on **Themes**.
3. Your current theme (called **Horizon**) is in the box at the top. Click the **⋯** (three dots)
   button beside the **Customize** button, and choose **Edit code**.
4. A code editor opens. On the left is a list of files. Under the **layout** folder, click
   **theme.liquid**.
5. Near the very top of the file, find the line that says **`<head>`**. It's usually line 3 or 4.
   You can also press **Cmd + F** and type `<head>` to find it.
6. Click at the **very end of that `<head>` line** and press **Return** to make a new, empty line
   under it.
7. **Copy everything in the grey box below** and paste it onto that empty line:

```liquid
{% unless request.design_mode %}
<script>
  /* We're Cured!: send visitors on to werecured.ca (see SHOP_LINKS.md in the website folder) */
  (function () {
    var path = location.pathname;
    if (/^\/(cart|checkout|checkouts|account|orders|policies|password|apps|tools|services)(\/|$)/.test(path)) return;
    var m = path.match(/\/products\/([^\/?#]+)/);
    location.replace('https://werecured.ca/' + (m ? '#product/' + m[1] : ''));
  })();
</script>
{% endunless %}
```

8. Click **Save** (top right). A green "Saved" message appears.

That's it. When you've done it, tell Claude and it will check from the outside that it's working.

## Trying it yourself

On your phone, open Instagram or Facebook, go to the **We're Cured!** shop and tap any piece, then
tap through to the website. You should land on werecured.ca with that piece open.

## If something looks wrong, or to undo it

Go back to the same file (steps 1–4) and delete the lines you pasted, from
`{% unless request.design_mode %}` down to `{% endunless %}`, then **Save**. Everything goes back
to exactly how it was.

Or use the **Older versions** link that appears above the code once a file has been saved:
choose the version from before today and save.

---

## Good to know (for later)

- **Customize screen still works.** The code doesn't run while you're in the theme's Customize
  screen, so that keeps working as normal (not that you need it).
- **New products work automatically.** Nothing to do when you add a batch.
- If you ever change the Shopify theme, the code goes with the old theme. It would need pasting
  into the new one.
