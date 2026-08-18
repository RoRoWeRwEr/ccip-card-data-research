# Credit Card Comparison Version 77 - Additive Ingestion Record

Generated: 2026-08-18.

## Decision and safety boundary

`Credit Card 77_260818_125243.pdf` is preserved byte-for-byte as a secondary, unverified social-media comparison source. It is not an official bank publication and cannot confirm or overwrite a populated master value. Existing workbook sheets, card rows, card IDs, formulas, confidence classifications, and conflicts remain unchanged.

## Source identity

- Displayed version: 77.
- Displayed update date: 2026-08-15.
- SHA-256: `8a51c97b8e1b3235f5799e05e41826d7ee7c420d1ef896af40691c4293f22902`.
- PDF pages: 1; one unusually large comparison canvas.
- Publisher branding: `credit_cards_sa` / `credit_cards23`.
- Authority: rank 9, secondary/unverified source.
- Embedded annotations: 15; supporting Google Drive documents: 13.

## Comparison coverage

The source contains category tables for Visa, Mastercard, cashback, Alfursan, travel/multi-loyalty products, digital banks/wallets, reward exclusions, and approximate reward-point values. It exposes useful schema leads for fees and waiver conditions, lounges, insurance, local/international rewards, points validity, cash withdrawal, foreign transaction fees, statement/due dates, welcome and milestone bonuses, exclusions, and redemption assumptions.

## Official follow-up: Tweeq and urpay

- Tweeq is an official entity/product lead. Its current official card terms identify a mada card with zero issuance and annual fees, SAR 10 replacement and delivery fees, and a 2% international transaction fee, with fees stated excluding VAT. No master row or ID was created.
- urpay/neoleap is an official entity/product-family lead. Current official terms identify Mada, Visa Platinum, Platinum Visitor, Alahli Club, and Visa Signature prepaid cards. Visa Signature terms state 1.2% local and 1.5% international cashback and enumerate exclusions. No master row or ID was created.

## Embedded-link classification

All 13 supporting Google Drive links were opened and inspected. They are single-page bank-specific exclusion summaries created in Apple Numbers and branded by the same social account. They cover Al Rajhi, Aljazira, SNB, ANB, Riyad, Emirates NBD, BSF, Albilad, Alinma, SAB, meem, Amex, and STC Bank. They are not official bank documents and are registered only as secondary leads.

## VAT reconciliation

The source says listed card fees include 15% VAT. Several values follow an exact VAT pattern: 2.00% becomes 2.30%, and fee bases of SAR 200/300/450/750/900/1,000 become SAR 230/345/517.50/862.50/1,035/1,150. This is a normalization hypothesis, not card-level evidence. It does not resolve the existing ANB 2.00% tariff versus 2.75% product-page conflict. Official urpay terms currently show 2.20% excluding VAT, whose mathematical VAT-inclusive equivalent is 2.53%, so the PDF column alignment must be validated before comparison.

## Additive outputs

- Workbook sheets: `CC77 Source Registry`, `CC77 Comparison Leads`, and `CC77 VAT Review`.
- Machine-readable files: `cc77_source_summary.json`, `cc77_embedded_links.csv/json`, `cc77_leads.csv/json`, and `cc77_vat_review.csv/json`.
- Staged comparison leads: 13.
- VAT review records: 5.
- Embedded supporting-link records: 13.
- Existing master rows overwritten: 0; deleted: 0; merged: 0.

## Required next work

Run separate identity-validation cycles for Tweeq and urpay before adding issuer or card IDs. For all other CC77 values, use the source only to locate current official tariffs, product pages, terms, and rewards documents. Never promote a CC77 value by itself.
