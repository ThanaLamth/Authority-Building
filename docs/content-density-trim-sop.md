# Content Density Trim -- SOP

> Workflow nay duoc rut ra tu viec chinh sua bai Coincu/01-top-tokenized-treasury-funds-2026 (2026-07-21).
> Ap dung cho moi bai top-list / review sau khi da pass article-outline-edit-sop.md.
> Chay SAU khi da them EEAT signals, scorecard, heading hierarchy.

---

## Nguyen tac goc (Pedro Dias, Google Search Quality)

Chat luong noi dung khong duoc do bang so luong tu. Mot noi dung duoc xem la chat luong khi no vuot qua ky vong cua nguoi doc -- nghia la nguoi doc giai quyet duoc van de nhanh hon ho nghi.

Bai viet chi co keo dai noi dung bang cac doan lan man ngay cang kho canh tranh. Google khong do so ky tu -- ho do nguoi dung da giai quyet duoc van de hay chua.

Ap dung vao Authority-Building network: moi site co reader profile khac nhau (xem writing-style-guide.md). Nguoi doc Coincu la fund analyst can so sanh 6 san pham trong 3 phut. Nguoi doc Coinlineup la beginner can biet chinh xac phai lam gi. Ca hai deu can bai ngan hon, khong phai bai dai hon.

---

## Khi nao chay SOP nay

- Bai da pass article-outline-edit-sop.md (co scorecard, heading hierarchy, EEAT signals)
- Bai co tong tu > 3,000w cho top-list 6-10 products
- Bai co bat ky paragraph nao > 45 words
- Bai co product sections > 200w ma structural comparison table da cover basic facts

---

## Buoc 1 -- Do luong hien trang

Chay script kiem tra:

```python
with open('article.md', 'r', encoding='utf-8') as f:
    content = f.read()

total_words = len(content.split())
print(f'Total: {total_words} words')

# Tim tat ca paragraph > 45w
paras = content.split('\n\n')
for i, p in enumerate(paras):
    p = p.strip()
    if not p or p.startswith('#') or p.startswith('|') or p.startswith('!') or p.startswith('*') or p.startswith('-') or p.startswith('>') or p.startswith('**'):
        continue
    wc = len(p.split())
    if wc > 45:
        print(f'OVER ({wc}w): {p[:100]}...')

# Word count tung product section
sections = content.split('### ')
for s in sections[1:]:
    title = s.split('\n')[0].strip()[:50]
    wc = len(s.split())
    print(f'  {wc:3d}w  ### {title}')
```

**Target:**
- Tong bai: <= 3,000w cho 6-product list, <= 4,000w cho 10-product list
- Moi product section: 150-200w
- Moi paragraph: <= 45 words
- 0 paragraphs OVER

---

## Buoc 2 -- Xac dinh prose thua: "table da noi roi"

Structural comparison table (## Structural comparison) da chua: issuer, underlying, access model, primary chain, redemption, management fee.

**Cat khoi product sections:** bat ky prose nao chi restate nhung facts nay. Vi du:

BAD (restate table):
> "OUSG is a tokenized fund share issued by Ondo Finance giving institutional investors exposure to short-term US Treasuries. Management fees are capped at 0.15% and waived until January 1, 2027."

GOOD (chi giu structural nuance + risk + EEAT):
> "OUSG's underlying portfolio is primarily held in BlackRock BUIDL. That creates a nested exposure to Securitize and BlackRock in addition to Ondo Finance as wrapper operator."

**Quy tac:** Neu thong tin da co trong bat ky table nao (summary, scorecard, structural comparison), khong lap lai trong prose. Prose chi giu:
1. Structural nuance ma table khong the dien dat
2. Risk angle
3. EEAT signal (governance vote, institutional integration, regulatory action, community signal)
4. Tension / "what this means" / forward question

---

## Buoc 3 -- Break paragraphs > 45w

Moi paragraph <= 45 words. Khong ngoai le.

Cach break:
- Tim cau co the tach thanh paragraph rieng (thuong la cau bat dau bang "That...", "In [date]...", "The fund...", "[Source] described...")
- Merge 2 paragraph qua ngan (<15w moi cai) neu chung phuc vu 1 y tuong
- Khong tao paragraph chi co 1 cau ngap ngung -- moi paragraph phai co 1 job ro rang

**Anti-pattern:** break thanh 13 micro-paragraphs (nhu USTB truoc khi fix) doc nhu bullet list gia dang prose. Ly tuong: 4-6 paragraphs moi product section.

---

## Buoc 4 -- Fold verification bloat

### "What this review verified and what it did not" table

Table nay thuong 150-200w va la verification theater -- fund analyst khong can biet screenshots da duoc capture.

**Thay bang:** 2-3 cau gop vao "Why you can trust this guide":

```markdown
## Why you can trust this guide

[1 cau: nguon du lieu chinh -- product pages, issuer docs, market data, ngay review]

[1 cau: tat ca product pages da verified + ngay cu the]

[1 cau: nhung gi KHONG verified -- subscription workflows, redemption, smart contract audits, jurisdiction eligibility. Can independent due diligence.]
```

Moi cau <= 45 words.

---

## Buoc 5 -- Fix cac section khac

Kiem tra va break paragraphs > 45w o:
- ## Analytical framework
- ## What this changes for market structure
- ## Scoring notes (thuong la 1 paragraph dai)
- Intro paragraph (## H2 dau tien)

---

## Buoc 6 -- Verify

Chay lai script Buoc 1. Ket qua can dat:

```
Total: [<= target]w
ALL PARAGRAPHS <= 45 WORDS

  177w  ### 1. Product A
  197w  ### 2. Product B
  ...
```

Neu con OVER, quay lai Buoc 3.

---

## Buoc 7 -- Commit

```bash
git add [file]
git commit -m "[Site] bai [XX]: trim product sections to ~180-200w, break all paragraphs <=45w, fold verification table, total [X]w (was [Y]w)"
git push
```

---

## Checklist truoc khi commit

- [ ] Tong tu <= target (3,000w cho 6-product, 4,000w cho 10-product)
- [ ] Moi product section 150-200w
- [ ] 0 paragraphs > 45 words
- [ ] Khong con prose restate structural comparison table
- [ ] Verification table da fold vao trust section (2-3 cau)
- [ ] Moi EEAT signal van con nguyen (governance vote, institutional integration, regulatory action, community signal)
- [ ] Moi risk angle van con nguyen
- [ ] Moi tension / forward question van con nguyen
- [ ] Internal links van con nguyen

---

## Nguyen tac bo sung tu Pedro

### Hoi nguoi doc, khong hoi Google
Thay vi doan Google muon gi, hoi nguoi doc: "Thong tin nao ban van chua tim thay?" Cau tra loi thuong la bang so sanh, video thuc te, hoac ban do -- khong phai them 2,000 tu prose.

### Chat luong giam dan theo thoi gian
Noi dung chinh xac hom nay se loi thoi sau 6-12 thang. Refresh cycle quan trong hon viet them bai moi. Moi bai trong Authority-Building network can Last updated date va refresh trigger (fees, chain support, availability, regulation status).

### Google do user satisfaction, khong do word count
Website nen hoc cach lang nghe nguoi dung thay vi chi lang nghe cac cong cu SEO. Google lien tuc khao sat nguoi dung de biet ket qua tim kiem nao thuc su huu ich.
