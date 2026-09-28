import glob

files = glob.glob("coinwy/swapzone-batch/articles/*.md") + \
        glob.glob("Kanalcoin/swapzone-batch/articles/*.md") + \
        glob.glob("DeFiLiban/swapzone-batch/articles/*.md")

# Use byte sequences
mojibake = {
    b"\xc2\xa0": b" ",
    b"\xe2\x80\x94": b"--",
    b"\xe2\x80\x93": b"-",
    b"\xe2\x80\x99": b"'",
    b"\xe2\x80\x98": b"'",
    b"\xe2\x80\x9c": b'"',
    b"\xe2\x80\x9d": b'"',
    b"\xe2\x98\x85": b"",
    b"\xe2\x80\xa6": b"...",
    b"\xc2\xae": b"(R)",
}

changed = 0
for path in files:
    with open(path, "rb") as fh:
        c = fh.read()
    orig = c
    for bad, good in mojibake.items():
        c = c.replace(bad, good)
    # Also decode and re-encode to normalize
    if c != orig:
        with open(path, "wb") as fh:
            fh.write(c)
        name = path.replace("\\", "/").split("/")[-1]
        print(f"Fixed: {name}")
        changed += 1

print(f"\nTotal fixed: {changed}")
