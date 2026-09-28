import codecs

filepath = r"C:\Users\admin\Authority-Building\coinwy\swapzone-batch\articles\11-swapzone-vs-changenow.md"

# Read with errors='replace' to handle bad bytes
with open(filepath, "r", encoding="utf-8", errors="replace") as f:
    content = f.read()

# Write back as clean UTF-8
with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Fixed encoding: {filepath}")
print(f"Content length: {len(content)}")
