import re

filepath = r"C:\Users\admin\Authority-Building\coinwy\swapzone-batch\articles\04-fixed-rate-vs-floating-rate-crypto-swap.md"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

new_block = """**What Reddit says**

Fixed-rate vs floating-rate debates appear regularly on [r/CryptoCurrency](https://www.reddit.com/r/CryptoCurrency/search/?q=fixed+rate+crypto+swap&sort=top). The community take is practical: use fixed-rate when you need the output amount to be predictable (paying someone a specific amount), use floating-rate when the market is calm and you want the slightly better average rate. Fixed-rate costs around 0.3 to 0.5% premium in most market conditions -- the question is whether predictability is worth that cost for your use case."""

# Replace the generic block
pattern = r'\*\*What Reddit says\*\*\r?\n\r?\nDiscussion about this topic on \[r/CryptoCurrency\][^\n]*\r?\n[^\n]*\r?\n[^\n]*'
new_content = re.sub(pattern, new_block, content)

if new_content != content:
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Fixed Art04")
else:
    print("No match - manual check")
    idx = content.find("What Reddit says")
    print(repr(content[idx:idx+300]))
