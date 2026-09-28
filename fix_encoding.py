import glob, re

files = glob.glob("coinwy/swapzone-batch/articles/*.md") + \
        glob.glob("Kanalcoin/swapzone-batch/articles/*.md") + \
        glob.glob("DeFiLiban/swapzone-batch/articles/*.md")

# Common mojibake from UTF-8 read as latin-1 then re-encoded
replacements = [
    ("\u00c2\u00a0", " "),       # non-breaking space
    ("\u00e2\u0080\u0094", "--"),  # em dash
    ("\u00e2\u0080\u0093", "-"),   # en dash  
    ("\u00e2\u0080\u0099", "'"),   # right single quote
    ("\u00e2\u0080\u0098", "'"),   # left single quote
    ("\u00e2\u0080\u009c", '"'),   # left double quote
    ("\u00e2\u0080\u009d", '"'),   # right double quote
    ("\u00e2\u0098\u0085", ""),    # star emoji (remove)
    ("\u00c3\u00a2", ""),          # â (garbled)
    # simpler patterns
    ("\u00c2\u00a0", " "),
    ("Â\u00a0", " "),
    ("â\u0080\u0094", "--"),
    ("â\u0080\u0099", "'"),
    ("â\u0080\u009c", '"'),
    ("â\u0080\u009d", '"'),
    ("Â—", "--"),
    ("Â\u2014", "--"),
    # Remove remaining Â artifacts
]

for path in files:
    with open(path, encoding="utf-8") as fh:
        c = fh.read()
    orig = c
    for bad, good in replacements:
        c = c.replace(bad, good)
    if c != orig:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(c)
        print(f"Fixed encoding: {path.split('/')[-1]}")

print("Done")
