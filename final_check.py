import glob, re

files = glob.glob("coinwy/swapzone-batch/articles/*.md") + \
        glob.glob("Kanalcoin/swapzone-batch/articles/*.md") + \
        glob.glob("DeFiLiban/swapzone-batch/articles/*.md")

issues = 0
for path in files:
    with open(path, "rb") as fh:
        raw = fh.read()
    c = raw.decode("utf-8")
    name = path.replace("\\", "/").split("/")[-1]
    
    # Check for remaining encoding artifacts
    bad_count = raw.count(b"\xc2\xa0") + raw.count(b"\xe2\x80\x94") + raw.count(b"\xe2\x98\x85")
    if bad_count > 0:
        print(f"ENCODING STILL BAD: {name} ({bad_count} artifacts)")
        issues += 1
    
    # Check for [INSERT or placeholder brackets
    placeholders = re.findall(r'\[INSERT[^\]]*\]|\[PLACEHOLDER\]|\[TBD\]', c)
    if placeholders:
        print(f"PLACEHOLDER found in {name}: {placeholders}")
        issues += 1
    
    # Count What users say blocks
    wus = c.count("**What users say**")
    mytake = c.count("My take:")
    
    if name.startswith(("05","06","07","08","09","10","11","12","13","14","15","16")):
        if wus == 0:
            print(f"NO BLOCKS: {name}")
            issues += 1

print(f"\nTotal issues: {issues}")
print("Article block summary:")
for path in sorted(files):
    with open(path, encoding="utf-8") as fh:
        c = fh.read()
    name = path.replace("\\", "/").split("/")[-1]
    if not name[0].isdigit():
        continue
    wus = c.count("**What users say**")
    mytake = c.count("My take:")
    print(f"  {name}: wus={wus} mytake={mytake}")
