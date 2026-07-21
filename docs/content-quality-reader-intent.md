# Content Quality Audit -- Reader Intent First

> Nguon: Pedro Dias (Google Search Quality).
> File nay duoc dung TRUOC KHI viet hoac edit bat ky bai nao.
> Muc dich: xac dinh reader intent that su, de bai viet chi chua nhung gi nguoi doc can -- khong hon, khong kem.

---

## Nguyen tac cot loi

Chat luong noi dung khong duoc do bang so luong tu.

Google khong bao gio noi bai 5.000 tu co loi the hon bai 1.000 tu. Chat luong la khai niem tuong doi: noi dung duoc xem la chat luong khi no vuot qua ky vong cua nguoi doc.

Dieu Google quan tam: nguoi dung da giai quyet duoc van de hay chua -- khong phai nguoi viet da go bao nhieu ky tu.

---

## Buoc 1 -- Xac dinh nguoi doc la ai

Truoc khi viet mot dong nao, tra loi 3 cau hoi:

1. **Nguoi doc dang o dau trong hanh trinh?**
   - Moi biet (dang tim hieu khai niem co ban)
   - Dang so sanh (da hieu, can chon giua cac lua chon)
   - Dang hanh dong (da chon, can buoc cu the de thuc hien)

2. **Ho can giai quyet van de gi cu the?**
   - Khong phai "ho muon biet ve tokenized treasuries"
   - Ma la "ho can biet nen chon BUIDL hay OUSG cho portfolio institutional cua ho"

3. **Ho se hai long khi nao?**
   - Khi ho co du thong tin de ra quyet dinh
   - Khi ho biet chinh xac buoc tiep theo la gi
   - Khi ho khong con phai mo tab khac de tim thong tin bo sung

**Vi du thuc te:**
- Query "Cach dang ky ho kinh doanh ca the" → nguoi doc can: ho so gi, nop o dau, bao lau co ket qua, loi thuong gap. Xong. Khong can 4.000 tu lich su phap luat.
- Query "top tokenized treasury funds 2026" → fund analyst can: so sanh 6 san pham theo structure/access/risk trong 3 phut. Khong can moi product restate issuer type ma table da noi.

---

## Buoc 2 -- Liet ke chinh xac nhung gi nguoi doc can biet

Viet ra danh sach cac cau hoi nguoi doc that su co. Khong them, khong bot.

**Format:**

```
Reader: [mo ta ngan]
Query intent: [informational / commercial comparison / transactional]
Ho can biet:
  1. [cau hoi cu the 1]
  2. [cau hoi cu the 2]
  3. [cau hoi cu the 3]
  ...
Ho KHONG can:
  - [thong tin thua ma thuong bi nhoi vao]
  - [thong tin thua khac]
```

**Vi du -- bai tokenized treasury funds:**
```
Reader: fund analyst, institutional allocator
Query intent: commercial comparison
Ho can biet:
  1. 6 san pham nao dang dinh nghia category nay?
  2. Chung khac nhau o dau (structure, access, risk)?
  3. San pham nao phu hop voi portfolio cua ho?
  4. Risk nao can flag cho due diligence?
  5. Institutional adoption evidence nao xac nhan tung san pham?
Ho KHONG can:
  - Restate issuer type, chain, fee ma table da chua
  - Giai thich US Treasury la gi
  - Lich su cua tokenization
  - 200 tu verification table liet ke screenshots da capture
```

---

## Buoc 3 -- Dinh luong: bao nhieu tu la du?

Khong co con so co dinh. Nhung co cong thuc:

**Moi don vi thong tin = 1 paragraph (max 45 words).**

Dem so don vi thong tin tu danh sach Buoc 2:
- 6 products x 4 don vi (nuance + risk + EEAT + tension) = 24 paragraphs product
- 1 analytical framework = 3-4 paragraphs
- 1 market structure implication = 3-4 paragraphs
- 1 trust section = 3 paragraphs
- Tables khong tinh vao word count target

→ ~30-35 paragraphs x 30-40w trung binh = 900-1,400w prose + tables = tong ~2,500-3,000w

**Nguyen tac:** Neu tong tu vuot qua target ma khong them thong tin moi, dang co van de padding.

---

## Buoc 4 -- Kiem tra: "Thong tin nao ban van chua tim thay?"

Loi khuyen cua Pedro: dung co doan Google muon gi. Hoi nguoi doc.

**Ap dung thuc te cho Authority-Building:**

Sau khi viet xong, doc lai bai voi con mat cua reader profile (tu writing-style-guide.md):

| Site | Hoi | Neu nguoi doc noi "chua du" thi thieu gi? |
| --- | --- | --- |
| Coincu | Fund analyst doc xong trong 3 phut co du de bat dau due diligence khong? | Thuong thieu: comparison table, risk flags, institutional adoption evidence |
| BitcoinMaximalist | Bitcoiner doc xong co biet chinh xac signing model nao phu hop khong? | Thuong thieu: spec table, air-gap comparison, setup friction |
| Coinlineup | Beginner doc xong co biet phai lam gi tiep theo khong? | Thuong thieu: step-by-step, plain-language glossary, "what NOT to do" |
| Kanalcoin | Nguoi dung o Hanoi/Jakarta doc xong co thay local fiat rails khong? | Thuong thieu: IDR/VND deposit, local regulation status, app store link |
| MarketBit | Trader doc xong co tim thay metric + mechanism + implication khong? | Thuong thieu: threshold callout, cross-metric validation |

**Neu khong the tu tra loi** cau hoi nay cho reader profile cu the, bai chua du tot de publish. Nhung giai phap la them thong tin dung -- khong phai them tu.

---

## Buoc 5 -- Nhan dien padding patterns

Nhung dau hieu bai dang bi keo dai vo ich:

| Pattern | Vi du | Fix |
| --- | --- | --- |
| Restate table data trong prose | "OUSG spans Ethereum, Solana, and Polygon" khi table da ghi Primary chain: Ethereum, Solana, Polygon | Xoa khoi prose |
| Giai thich khai niem nguoi doc da biet | "US Treasury bills are short-term government debt instruments" cho fund analyst | Xoa |
| Verification theater | 200w table liet ke screenshots da capture | Fold thanh 2-3 cau trong trust section |
| Transition sentences khong mang thong tin | "Let's now take a closer look at each product" | Xoa |
| Restate ket luan cua paragraph truoc | "As mentioned above, BUIDL's collateral acceptance..." | Xoa |
| Padding adjectives | "very important", "extremely significant", "highly notable" | Xoa adjective, giu fact |
| Filler context | "In the rapidly evolving world of tokenized assets..." | Xoa ca cau |

---

## Buoc 6 -- Chat luong giam dan theo thoi gian

Noi dung chinh xac hom nay se loi thoi. Khong co bai viet nao "xong" vinh vien.

**Refresh triggers -- kiem tra moi 3-6 thang:**
- Fees thay doi
- Chain support them/bot
- Regulatory status thay doi
- AUM/TVL thay doi > 20%
- San pham moi gia nhap category
- San pham cu ngung hoat dong
- Onboarding/payment flow thay doi

**Khi refresh:** cap nhat Last updated date, cap nhat facts trong table + prose, xoa san pham khong con relevant, them san pham moi neu du tieu chi.

---

## Tom tat

```
Truoc khi viet:
  1. Xac dinh nguoi doc la ai va ho can gi (Buoc 1-2)
  2. Dinh luong bao nhieu tu la du (Buoc 3)

Trong khi viet:
  3. Chi viet nhung gi nguoi doc can, khong restate table data
  4. Moi paragraph <= 45 words, moi paragraph co 1 job

Sau khi viet:
  5. Doc lai voi con mat reader: "Thong tin nao van chua tim thay?" (Buoc 4)
  6. Scan padding patterns va xoa (Buoc 5)
  7. Dat refresh trigger (Buoc 6)
```

Bai viet ngan hon ma giai quyet van de nhanh hon = bai viet tot hon.
Google do user satisfaction, khong do word count.
