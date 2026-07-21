# Article Outline Edit & AI Footprint Removal -- SOP

> Workflow này được rút ra từ việc chỉnh sửa bài 01-02-03 của BitcoinMaximalist (2026-07-20).
> Áp dụng cho mọi bài top-list / review trước khi publish.

---

## Mục tiêu

1. Bổ sung cấu trúc scannable ở đầu bài (quick comparison + scorecard)
2. Tổ chức lại heading hierarchy cho đúng
3. Dời section editorial xuống cuối bài
4. Xóa sạch mọi dấu hiệu AI drafting note / placeholder

---

## Bước 1 -- Thêm Quick Comparison Table

**Vị trí:** Ngay sau đoạn "Bottom line: ..." của intro, trước bất kỳ H2 nào.

**Cột cần có (top-list review):**

| Cột | Ý nghĩa |
| --- | --- |
| Product name | Tên ngắn gọn |
| Price / Cost | Giá hoặc free/paid |
| Best for | 3-5 từ mô tả đối tượng chính |
| Key differentiator | 1 điểm nổi bật nhất (air-gap, custody model, v.v.) |
| Open source | Yes / Partial / No |
| Difficulty / Setup | Easy / Moderate / High / DIY |

Số cột có thể điều chỉnh theo topic (lightning wallet dùng "Node required", multisig dùng "Key control", v.v.)

---

## Bước 2 -- Thêm Ranking Scorecard

**Vị trí:** Ngay sau Quick Comparison table.

**Format:**

```markdown
## Ranking scorecard

Scored out of 10 per category. Total out of [N*10].

| Product | Criteria 1 | Criteria 2 | ... | **Total** |
| --- | --- | --- | --- | --- |
| Product A | 9 | 8 | ... | **XX** |
```

**Tiêu chí chọn:** 6-7 criteria phù hợp với topic. Ví dụ:
- Hardware wallet: Security model, Setup ease, Value for money, Bitcoin focus, Open source, Air-gap, Multisig & interop → /70
- Lightning wallet: Sovereignty, Ease of use, Liquidity UX, Feature range, Open source, Node control → /60
- Multisig: Sovereignty, Ease of setup, Recovery model, Open source, HW compatibility, Cost → /60

**Bắt buộc thêm:** Đoạn "Scoring notes" giải thích từng tiêu chí + 1-2 câu tóm tắt kết quả (ai dẫn đầu, tại sao product có score cao nhất không phải top pick).

---

## Bước 3 -- Thêm H2 "X Best [Topic] Reviewed (2026 List)"

**Vị trí:** Ngay trước section đầu tiên review từng product (trước ### Product 1).

**Format:**
```markdown
## X Best [Topic] Reviewed (2026 List)

If you are still exploring the broader [topic] landscape, you can compare these picks against [internal link 1] or [internal link 2].

Here, we dive deep into the [X] best [topic], analysing their [criteria list] to help you identify the right [product type] for your [use case].
```

Điều chỉnh internal links theo site's sitemap. Số X = số product review trong bài.

---

## Bước 4 -- Hạ Heading Wallet/Product từ H2 → H3

Mỗi product được review riêng phải là H3, không phải H2.

- `## Coldcard` → `### Coldcard`
- `## Phoenix` → `### Phoenix`
- v.v.

**Giữ nguyên H2** cho: section intro, comparison table, scorecard, editorial sections, FAQ.

---

## Bước 5 -- Di chuyển "What we checked" Block xuống trước FAQ

**Block cần di chuyển gồm 2 phần:**
1. `## What we checked ourselves before ranking these [products]` + content
2. `## What this review verified and what it did not` + bảng Verified/Not verified

**Từ:** Vị trí hiện tại (thường ngay sau intro hoặc ngay sau bottom line)
**Đến:** Ngay trước `## Frequently asked questions`

---

## Bước 6 -- Xóa AI Footprint

Scan và xóa tất cả các loại sau:

### 6a. Blockquote "Why you can trust this guide"
```
> **Why you can trust this guide**
> This draft is based on...
```
→ Xóa toàn bộ blockquote.

### 6b. Câu "screenshots should not sit silently"
Thường nằm trong "What we checked" block:
```
The screenshots above should not sit silently in the article. They should show/help...
```
→ Xóa câu đó.

### 6c. Template table với [insert ...] placeholders
```
If your team runs direct tests / live checks / setup checks, add a measured comparison...

| ... | `[insert measured time]` | `[insert note]` |
```
→ Xóa toàn bộ đoạn đó kể cả table.

### 6d. "If your team hits a real issue" block
```
If your team hits a real issue, document it plainly / directly:
- what failed
- how often it happened
...
That kind of troubleshooting detail is one of the strongest trust signals...
```
→ Xóa toàn bộ đoạn + bullet list + câu kết.

### 6e. "This section should not read like PR copy"
```
This section should not read like PR copy. A page that only praises...
```
→ Xóa câu đó (thường là câu mở đầu của risks section).

### 6f. "If this article is upgraded with real test data later"
```
If this article is upgraded with real test data later, this is the section where direct language should appear:
- `We reviewed the setup flow and noticed...`
...
```
→ Xóa toàn bộ đoạn + code-style bullet list.

---

## Scan nhanh để kiểm tra còn sót không

Sau khi chỉnh, search các phrase sau trong file -- nếu match là còn sót:

```
your team
insert wallet
insert product
insert measured
insert note
insert count
This draft
upgraded with real
screenshots above should not
document it plainly
document it directly
this article is upgraded
[insert
should not read like PR copy
For the final publish version
```

---

## Checklist hoàn chỉnh trước khi commit

- [ ] Quick comparison table đặt đúng chỗ (sau bottom line, trước H2 đầu tiên)
- [ ] Ranking scorecard có scoring notes giải thích
- [ ] H2 "X Best ... Reviewed" xuất hiện trước product đầu tiên
- [ ] Tất cả product heading là H3
- [ ] "What we checked" block nằm ngay trước FAQ
- [ ] Không còn blockquote "Why you can trust"
- [ ] Không còn placeholder [insert ...] nào
- [ ] Không còn câu "if your team..."
- [ ] Scan sạch theo danh sách phrase ở trên

