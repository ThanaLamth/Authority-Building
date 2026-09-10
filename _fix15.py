import re, os

fp = r"C:\Users\admin\Authority-Building\CCpress\changenow-batch\articles\15-changenow-api-review-2026.md"
content = open(fp, encoding="utf-8").read()

# 1. Replace em dashes (—) with commas in the What Users Report block
# Find the section boundaries
start = content.find("What Users Report")
next_h2 = content.find("\n## ", start + 1)
section = content[start:next_h2]

# Replace — with , in that section only
section_fixed = section.replace("\u2014", ",")

# 2. Add Trustpilot links to Jonathan B and Roman
jonathan_url = "https://www.trustpilot.com/reviews/6a83070692d5b9770ea69a95"
roman_url    = "https://www.trustpilot.com/review/changenow.io"

section_fixed = section_fixed.replace(
    "**Jonathan B (Trustpilot):**",
    f"**[Jonathan B (Trustpilot)]({jonathan_url}):**"
)
section_fixed = section_fixed.replace(
    "**Roman (Trustpilot, critical):**",
    f"**[Roman (Trustpilot, critical)]({roman_url}):**"
)

new_content = content[:start] + section_fixed + content[next_h2:]

open(fp, "w", encoding="utf-8").write(new_content)
print("Done. Checking result...")

# Verify
c2 = open(fp, encoding="utf-8").read()
idx = c2.find("What Users Report")
print(c2[idx:idx+800])
