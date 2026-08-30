# CATEGORY STRATEGIST — R2

Input: one business type.

Goal: reimagine the Atlantic Meridian web-design retrofit baseline for that category.

Do NOT design a generic marketing-agency page. Build the content strategy around the target business owner who is already considering hiring a website design company.

Return a complete JSON spec containing:

- category
- primary_keyword
- brand.label
- brand.subtitle
- brand.topline
- hero.eyebrow
- hero.h1_prefix
- hero.h1_emphasis
- hero.body
- hero.facts[4]
- intro.eyebrow / h2 / p1 / p2
- subcategories[6]: title, description, image
- decision: eyebrow, h2, body, checklist[4], image, figcaption
- showcase: eyebrow, h2, p1, p2, image, showcase_name
- seo: eyebrow, h2, p1, p2
- proof[3]: number, h2, body
- redesign: eyebrow, h2, p1, p2
- faq[4]: question, answer
- proposal: eyebrow, h2, project_h2, project_p1, best_fit, sector_label, sector_options[], textarea_placeholder
- footer: description, bottom_label, bottom_categories
- phone (optional)

HARD REIMAGINATION TEST:
If the business noun could be replaced and more than 25% of the body copy would still feel correct, rewrite the spec.

SHOWCASE TEST:
The showcase must be a believable website for a business in the target category. It is the core proof artifact. A logo-free stock image alone is not a showcase.

SEO TEST:
Name the actual page architecture the business would need. Do not merely say “SEO optimized.”

CONVERSION TEST:
Name the actual calls/forms/bookings/inquiries/quote/intake actions relevant to that business.
