#!/usr/bin/env python3
"""Save a snapshot of every live product — price, type, weight, SKU, stock.

Used to compare the shop before and after a round of edits, so Janet can make all
her changes in Shopify and Claude can then show her exactly what moved.

    python3 shopify/snapshot.py              # write shopify/price-snapshot.json
    python3 shopify/snapshot.py --diff       # compare the live shop against that file

Only reads. Sees published products only — anything switched to Draft drops out of view.
"""
import json, os, sys, urllib.request, datetime

TOKEN = "4b5f552cdecea53a71057cf281cdd532"
URL   = "https://fbkwka-jw.myshopify.com/api/2024-10/graphql.json"
HERE  = os.path.dirname(os.path.abspath(__file__))
SNAP  = os.path.join(HERE, "price-snapshot.json")

QUERY = """query($c:String){ products(first:100, after:$c){
  pageInfo{ hasNextPage endCursor }
  edges{ node{ title handle productType
    variants(first:1){ edges{ node{ sku weight weightUnit availableForSale
      price{ amount } } } } } } } }"""

def fetch():
    out, cursor = {}, None
    while True:
        req = urllib.request.Request(URL,
            data=json.dumps({"query": QUERY, "variables": {"c": cursor}}).encode(),
            headers={"X-Shopify-Storefront-Access-Token": TOKEN,
                     "Content-Type": "application/json"})
        conn = json.load(urllib.request.urlopen(req))["data"]["products"]
        for e in conn["edges"]:
            n = e["node"]
            v = n["variants"]["edges"][0]["node"] if n["variants"]["edges"] else {}
            w, u = v.get("weight") or 0, v.get("weightUnit") or ""
            out[n["handle"]] = {
                "title": n["title"], "type": n["productType"],
                "price": float(v.get("price", {}).get("amount", 0)),
                "grams": (round(w * 1000) if u == "KILOGRAMS" else round(w)) if w else None,
                "sku": v.get("sku") or "", "forSale": v.get("availableForSale"),
            }
        if not conn["pageInfo"]["hasNextPage"]:
            return out
        cursor = conn["pageInfo"]["endCursor"]

def diff(old, new):
    lines, FIELDS = [], [("price","price","$"),("type","type",""),("grams","weight"," g"),
                         ("title","title",""),("forSale","for sale","")]
    for h, n in sorted(new.items(), key=lambda kv: kv[1]["title"].lower()):
        o = old.get(h)
        if o is None:
            lines.append("NEW      %-44s %-20s $%.0f" % (n["title"][:44], n["type"], n["price"]))
            continue
        for key, label, unit in FIELDS:
            a, b = o.get(key), n.get(key)
            if a != b:
                fmt = (lambda v: "—" if v is None else
                       ("$%.0f" % v if key == "price" else "%s%s" % (v, unit)))
                lines.append("%-8s %-44s %s: %s -> %s"
                             % ("CHANGED", n["title"][:44], label, fmt(a), fmt(b)))
    for h, o in sorted(old.items(), key=lambda kv: kv[1]["title"].lower()):
        if h not in new:
            lines.append("GONE     %-44s (unpublished, renamed handle, or deleted)" % o["title"][:44])
    return lines

if __name__ == "__main__":
    live = fetch()
    if "--diff" in sys.argv:
        if not os.path.exists(SNAP):
            sys.exit("No snapshot to compare against. Run without --diff first.")
        saved = json.load(open(SNAP))
        rows = diff(saved.get("products", saved), live)
        print("Compared against snapshot of %s\n" % saved.get("taken", "unknown date"))
        print("\n".join(rows) if rows else "Nothing has changed.")
        print("\n%d product(s) live." % len(live))
    else:
        json.dump({"taken": datetime.date.today().isoformat(), "products": live},
                  open(SNAP, "w"), indent=1, sort_keys=True)
        print("Snapshot saved: %d products -> %s" % (len(live), SNAP))
