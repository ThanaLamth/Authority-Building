import re, os

fp = r"C:\Users\admin\Authority-Building\CCpress\changenow-batch\articles\16-is-changenow-legit-2026.md"
content = open(fp, encoding="utf-8").read()

start = content.find("What Users Report")
next_h2 = content.find("\n## ", start + 1)
section = content[start:next_h2]

# Replace em dashes with commas
section_fixed = section.replace("\u2014", ",")
# Fix space before comma
section_fixed = re.sub(r"\s+,", ",", section_fixed)

# Add Trustpilot links
jonathan_url = "https://www.trustpilot.com/reviews/6a83070692d5b9770ea69a95"
roman_url    = "https://www.trustpilot.com/review/changenow.io"

section_fixed = section_fixed.replace(
    "**Jonathan B (Trustpilot, positive):**",
    f"**[Jonathan B (Trustpilot, positive)]({jonathan_url}):**"
)
section_fixed = section_fixed.replace(
    "**Roman (Trustpilot, critical):**",
    f"**[Roman (Trustpilot, critical)]({roman_url}):**"
)

new_content = content[:start] + section_fixed + content[next_h2:]
open(fp, "w", encoding="utf-8").write(new_content)
print("Art 16 patched.")
idx = new_content.find("What Users Report")
print(new_content[idx:idx+900])
