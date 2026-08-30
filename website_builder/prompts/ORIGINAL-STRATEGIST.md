# ORIGINAL MODE STRATEGIST — R3

Given a business, create a business-native website plan rather than adapting a fixed template.

Return a JSON spec for `runtime/build_original.py` with:
- `mode: original`
- `business`: name, type, location, phone/email/address when known
- `navigation`: page label + filename
- `hero`: business-native first-fold copy, CTA, and LOCAL image path
- `pages`: each page gets distinct purpose, title, H1, intro, and sections
- section types: `text`, `split`, `cards`, `gallery`, `contact`
- imagery must be semantically owned by the section and stored locally before production

Hard rules:
1. Do not invent reviews, credentials, awards, licenses, addresses, statistics or customer results.
2. Do not force every business into the same page architecture.
3. Do not pad copy to hit word counts; add decision-useful information.
4. The homepage first fold must feel like the business, not like an agency template.
5. Image sources can be researched upstream (for example Pexels), but final build paths must be local.
6. Desktop and mobile screenshots must be visually reviewed before release.
