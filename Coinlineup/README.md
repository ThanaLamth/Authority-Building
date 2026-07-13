# Coinlineup Authority-Building Package

This folder contains the first Coinlineup beginner-explainer list batch prepared on 2026-07-10.

## Contents

- `articles/`
  - 10 draft list/explainer articles for the new evergreen guides and projects clusters
- `media/`
  - captured public-page evidence images and custom comparison graphics used to support the article batch
- `html/`
  - WordPress-ready HTML fragments exported from the markdown drafts
- `payloads/`
  - JSON payloads per article with title, slug, meta description, HTML body, schema, internal links, external references, and media
- `export_coinlineup.py`
  - package-specific exporter used to generate the HTML and payload batch
- `coinlineup-content-tracker-2026-07-10.md`
  - status tracker for the batch

## Editorial rules used

- The first `H2` answers the title directly.
- The rest of the article follows a chained explanatory flow:
  answer -> method -> list -> evidence -> what it means -> FAQ.
- Tone stays plain-English and beginner-friendly.
- Rankings avoid hype language and call out risks directly.

## Notes

- These drafts are written to be publish-ready in structure, but live prices, market caps, and exchange availability should still be checked again on the day of publication.
- Public-page screenshots captured on `2026-07-13` are stored in `media/` and referenced inside the article drafts.
- Each article now also has one custom SVG comparison graphic stored in `media/` and embedded near the first-hand review section.
- Internal links are listed as target URLs so the CMS team can map them once the supporting pages exist.
- The exporter rewrites article media to raw GitHub URLs under `https://raw.githubusercontent.com/ThanaLamth/Authority-Building/main/Coinlineup/media/...` so the HTML fragments are immediately usable in a CMS draft.
- JSON payloads use `{{SITE_URL}}` placeholders inside `schema_jsonld` for canonical article URLs.

## Export workflow

- Run `python3 Coinlineup/export_coinlineup.py` from the repo root to regenerate `html/` and `payloads/`.
- Import the `content_html` value from each payload into the CMS body field.
- Use the payload `title`, `slug`, `meta_title`, `meta_description`, and `schema_jsonld` fields to complete the CMS entry.
