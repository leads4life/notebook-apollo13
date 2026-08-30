# BUSINESS WEBSITE COMPOSER R3

**Current main website builder.**

R3 unifies two production paths under one controlled system:

- **ORIGINAL** — create a new customer website from business/industry/brand inputs.
- **RETROFIT** — preserve the strongest design/composition DNA from an approved reference and reimagine it for a different business/category.
- **AUTO** — route to ORIGINAL when no approved reference is supplied; route to RETROFIT when an approved reference/baseline is supplied.

## Lineage

R3 promotes the successful `CATEGORY-RETROFIT-LANDING-ENGINE-R2` into a broader business website composer. The R2 retrofit renderer is preserved as `website_builder/runtime/build_retrofit.py`; it is not overwritten.

First ORIGINAL benchmark: **Café Brisa Vieja — Havana Cuban coffee shop**.

## Run

```bash
python website_builder/runtime/build.py spec.json --output ./build
```

Optional explicit mode override:

```bash
python website_builder/runtime/build.py spec.json --output ./build --mode original
python website_builder/runtime/build.py spec.json --output ./build --mode retrofit
python website_builder/runtime/build.py spec.json --output ./build --mode auto
```

## Production contract

1. Determine ORIGINAL / RETROFIT / AUTO route.
2. Build category/business strategy before layout generation.
3. Use semantic image slots; production assets must be local.
4. Render responsive desktop + mobile output.
5. Human-eye visual QA is a hard final gate.
6. Repair and re-render until the actual pixels pass.
7. Package production ZIP + self-contained preview when requested.

The current source lives in `website_builder/`.
