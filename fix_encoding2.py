import glob

files = glob.glob("coinwy/swapzone-batch/articles/*.md") + \
        glob.glob("Kanalcoin/swapzone-batch/articles/*.md") + \
        glob.glob("DeFiLiban/swapzone-batch/articles/*.md")

# More aggressive: find and fix any remaining misencoded bytes
def fix(c):
    # Most common artifacts from latin-1 misread
    fixes = [
        ("\u00c2\u00a0", " "),
        ("\u00c2\u00ae", "(R)"),
        ("\u00e2\u0080\u0094", "--"),
        ("\u00e2\u0080\u0093", "-"),
        ("\u00e2\u0080\u0099", "'"),
        ("\u00e2\u0080\u0098", "'"),
        ("\u00e2\u0080\u009c", '"'),
        ("\u00e2\u0080\u009d", '"'),
        ("\u00e2\u0098\u0085", ""),
        ("\u00e2\u0080\u00a6", "..."),
        # Also check for byte sequences that got double-encoded
        ("â€™", "'"), ("â€˜", "'"),
        ("â€œ", '"'), ("â€\x9d", '"'),
        ("â€"", "--"), ("â€"", "--"),
        ("â€¦", "..."),
        ("Ã©", "e"), ("Ã¨", "e"),
        # star artifacts
        ("â˜…", ""), ("â˜†", ""),
    ]
    for bad, good in fixes:
        c = c.replace(bad, good)
    return c

changed = 0
for path in files:
    with open(path, encoding="utf-8") as fh:
        c = fh.read()
    fixed = fix(c)
    if fixed != c:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(fixed)
        print(f"Fixed: {path.split('/')[-1]}")
        changed += 1

print(f"\nTotal fixed: {changed}")
