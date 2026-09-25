#!/usr/bin/env python3
"""Rebuild the printable stock sheet from the live shop.

    python3 shopify/stock_sheet.py            # refresh from Shopify, rewrite stock-sheet.html
    python3 shopify/stock_sheet.py --cached   # use the saved snapshot instead of calling Shopify

Only reads. Replaces the data block inside stock-sheet.html and leaves the rest of the
page — layout, print styles, the wording in the footer — exactly as it was.

Print from the copy on the Mac, not the web copy: the browser won't start a print from
inside a page that's embedded somewhere else.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SHEET = os.path.join(HERE, "stock-sheet.html")
SNAP = os.path.join(HERE, "price-snapshot.json")

# The order the sheet lays the sections out in; anything else falls to the end.
ORDER = ["Coasters", "Bowls and Platters", "Home Decor", "Pendant", "Earrings"]


def load():
    if "--cached" in sys.argv:
        return json.load(open(SNAP))["products"]
    sys.path.insert(0, HERE)
    import snapshot
    return snapshot.fetch()


def main():
    products = load()
    rows = [{"t": p["title"], "c": p["type"], "s": p["sku"],
             "p": p["price"], "g": p["grams"], "a": p["forSale"]}
            for p in products.values()]
    rows.sort(key=lambda r: ((ORDER.index(r["c"]) if r["c"] in ORDER else 99),
                             r["t"].lower()))

    html = open(SHEET).read()
    block = json.dumps(rows, ensure_ascii=True)
    new, n = re.subn(
        r'(<script id="data" type="application/json">).*?(</script>)',
        lambda m: m.group(1) + block + m.group(2),
        html, count=1, flags=re.S)
    if n != 1:
        sys.exit("Could not find the data block in stock-sheet.html — nothing written.")
    open(SHEET, "w").write(new)

    missing = sum(1 for r in rows if r["g"] is None)
    print(f"Stock sheet rebuilt: {len(rows)} products, "
          f"{missing} still without a weight, "
          f"${sum(r['p'] for r in rows):,.0f} listed value")
    for cat in ORDER:
        c = sum(1 for r in rows if r["c"] == cat)
        if c:
            print(f"  {cat:<20} {c:>4}")


if __name__ == "__main__":
    main()
