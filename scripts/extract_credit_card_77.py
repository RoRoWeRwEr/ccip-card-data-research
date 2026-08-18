#!/usr/bin/env python3
"""Extract non-destructive staging evidence from Credit Card comparison version 77.

The social-media comparison PDF is preserved as an immutable secondary source.
This script records source metadata, embedded links, research leads, and VAT
reconciliation hypotheses. It never updates a master card row or raw source.
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Credit Cards Terms and Conditions" / "Credit Card 77_260818_125243.pdf"
MACHINE = ROOT / "outputs" / "machine-readable"
REPORT = ROOT / "outputs" / "reports" / "CREDIT_CARD_77_INGESTION.md"
EXPECTED_SHA256 = "8a51c97b8e1b3235f5799e05e41826d7ee7c420d1ef896af40691c4293f22902"
EXTRACTED_ON = "2026-08-18"


SUPPORTING_LINKS = [
    ("Al Rajhi Bank", "استثناءات الراجحي", "39d1ff2baec2df53972e7cb13985eb64ca47f8dd43ad02413edafc4dedd5f081", "2025-06-21"),
    ("Bank Aljazira", "استثناءات الجزيرة", "1930ba10554ce57de6566c83f4bba0a435446d95acf9b3d1e258e24316ca067c", "2025-07-15"),
    ("Saudi National Bank", "استثناءات الأهلي", "7d788151fc1f478e78528d824ca804d0c2bbe6cfd83f282fb51ce75200b6d854", "2024-09-10"),
    ("Arab National Bank", "استثناءات العربي", "da8bed482da723502a7231f7fc845673c3953e97ea938c27f0be78cf5be1160c", "2025-07-16"),
    ("Riyad Bank", "استثناءات الرياض", "9769b0023086868bff8b4d5d2fe04a3e60cc751ff52c0bcd31250147f8ae6f40", "2025-08-28"),
    ("Emirates NBD KSA", "استثناءات الإمارات دبي", "6f777f8ae636cd021060e26c2daee36a7913a31c63b3102e604451c326b0a748", "2025-07-21"),
    ("Banque Saudi Fransi", "استثناءات الفرنسي", "9223453a10d2a46c4108d2e6918162083704739dbcc1d6e5f148523e84f71371", "2026-01-04"),
    ("Bank Albilad", "استثناءات البلاد", "db9ca2c8e5f7886ceb8f767d8c734bbb1f38b145f94c3a185a8ee309f5fd210c", "2025-09-25"),
    ("Alinma Bank", "استثناءات الإنماء", "800a91f1a7cf7aa7c7f56261cee5aeb7ea10e0d6321248fd539715b9d3b45b60", "2024-09-10"),
    ("Saudi Awwal Bank", "استثناءات الأول", "03ada62d56516b964e3d065089533cb4d5a4165275836658eb96e7923593a093", "2025-07-14"),
    ("Gulf International Bank Saudi Arabia (meem)", "استثناءات ميم", "da22b0f674a777c677f88ef61bb4c94a25faaeb395068fdfbec166f471f0ccf1", "2026-04-23"),
    ("American Express Saudi Arabia", "استثناءات أميكس", "f1eba4ffad5acaaabca24d1fc1a9b000cfb31feb94e179a4a2da0f3dd3d8cd3b", "2024-09-06"),
    ("STC Bank", "استثناءات STCBank", "69bd54ec0641c974b936c3aa5af5e86dfbbdc1a2df109eef1ff97a7a1264261c", "2026-04-03"),
]


LEADS = [
    {
        "lead_id": "CC77-L001", "entity": "Tweeq", "candidate_product": "Tweeq mada Card",
        "lead_type": "new_entity_and_product_candidate", "pdf_evidence": "Digital banks and wallets comparison",
        "official_evidence": "Official terms list mada card: issuance SAR 0, annual SAR 0, replacement SAR 10, delivery SAR 10, international transaction fee 2%, all excluding VAT.",
        "official_url": "https://tweeq.sa/en/payment-cards-terms-conditions",
        "status": "official_candidate_unmerged", "recommended_action": "Create a separate identity-validation task; do not add to master until scope, licensing identity, network/co-badge, and current availability are confirmed.",
    },
    {
        "lead_id": "CC77-L002", "entity": "urpay / neoleap", "candidate_product": "urpay card portfolio",
        "lead_type": "new_entity_candidate", "pdf_evidence": "Digital banks and wallets comparison",
        "official_evidence": "Official card terms confirm prepaid cards directly debiting the SAR wallet and identify multiple card products.",
        "official_url": "https://www.urpay.com.sa/en/cards-terms-conditions",
        "status": "official_candidate_unmerged", "recommended_action": "Validate legal entity, licensing name, and whether CCIP treats urpay as a separate issuer/entity before adding products.",
    },
    {
        "lead_id": "CC77-L003", "entity": "urpay / neoleap", "candidate_product": "urpay Mada Card",
        "lead_type": "new_product_candidate", "pdf_evidence": "Digital banks and wallets comparison",
        "official_evidence": "Virtual issuance free; annual fee free; supplementary SAR 30; physical printing SAR 30.",
        "official_url": "https://www.urpay.com.sa/en/cards-terms-conditions",
        "status": "official_candidate_unmerged", "recommended_action": "Validate current application availability and identity before assigning a card_id.",
    },
    {
        "lead_id": "CC77-L004", "entity": "urpay / neoleap", "candidate_product": "urpay Visa Platinum Card",
        "lead_type": "new_product_candidate", "pdf_evidence": "Digital banks and wallets comparison",
        "official_evidence": "Virtual issuance free; annual fee free; supplementary SAR 30; physical printing SAR 30.",
        "official_url": "https://www.urpay.com.sa/en/cards-terms-conditions",
        "status": "official_candidate_unmerged", "recommended_action": "Validate current application availability and card-level cashback rules before assigning a card_id.",
    },
    {
        "lead_id": "CC77-L005", "entity": "urpay / neoleap", "candidate_product": "urpay Platinum Visitor Card",
        "lead_type": "new_product_candidate", "pdf_evidence": "Not separately identifiable in CC77 table",
        "official_evidence": "Official terms list virtual issuance and annual fee as free; supplementary and physical printing are N/A.",
        "official_url": "https://www.urpay.com.sa/en/cards-terms-conditions",
        "status": "official_candidate_unmerged", "recommended_action": "Confirm eligibility and whether the product remains actively issued.",
    },
    {
        "lead_id": "CC77-L006", "entity": "urpay / neoleap", "candidate_product": "urpay Alahli Club Card",
        "lead_type": "new_product_candidate", "pdf_evidence": "Not separately identifiable in CC77 table",
        "official_evidence": "Official terms list SAR 30 virtual issuance, annual, and supplementary fees; SAR 70 physical printing.",
        "official_url": "https://www.urpay.com.sa/en/cards-terms-conditions",
        "status": "official_candidate_unmerged", "recommended_action": "Confirm current availability and co-brand identity before assigning a card_id.",
    },
    {
        "lead_id": "CC77-L007", "entity": "urpay / neoleap", "candidate_product": "urpay Visa Signature Card",
        "lead_type": "new_product_candidate", "pdf_evidence": "Digital banks and wallets comparison",
        "official_evidence": "SAR 300 virtual issuance, annual, and supplementary fees; SAR 30 physical printing; cashback 1.2% local and 1.5% international; exclusions listed in official terms.",
        "official_url": "https://www.urpay.com.sa/en/cards-terms-conditions",
        "status": "official_candidate_unmerged", "recommended_action": "Validate current availability and normalize cashback exclusions before assigning a card_id.",
    },
    {
        "lead_id": "CC77-L008", "entity": "Multi-bank", "candidate_product": "Statement and due-date fields",
        "lead_type": "schema_enrichment_candidate", "pdf_evidence": "Visa, Mastercard, cashback, Alfursan and travel tables",
        "official_evidence": "Not validated bank-by-bank in this task.", "official_url": "",
        "status": "secondary_lead_only", "recommended_action": "Add atomic statement_date_basis and payment_due_date_basis fields only after official verification.",
    },
    {
        "lead_id": "CC77-L009", "entity": "Multi-bank", "candidate_product": "Fee-waiver conditions",
        "lead_type": "schema_enrichment_candidate", "pdf_evidence": "Annual fee and spend-waiver rows",
        "official_evidence": "Not validated bank-by-bank in this task.", "official_url": "",
        "status": "secondary_lead_only", "recommended_action": "Separate standard fee, promotional fee, first-year fee, renewal fee, VAT basis, waiver threshold, and customer segment.",
    },
    {
        "lead_id": "CC77-L010", "entity": "Multi-bank", "candidate_product": "Rewards valuation assumptions",
        "lead_type": "calculation_model_candidate", "pdf_evidence": "Points-value and example-spend sections",
        "official_evidence": "PDF states flight values are approximate and vary by destination and price.", "official_url": "",
        "status": "secondary_lead_only", "recommended_action": "Keep redemption values time-stamped, channel-specific, and separate from direct earning rates.",
    },
    {
        "lead_id": "CC77-L011", "entity": "Multi-bank", "candidate_product": "Reward exclusions",
        "lead_type": "missing_data_and_conflict_lead", "pdf_evidence": "13 linked exclusion summaries",
        "official_evidence": "Linked PDFs are social-account summaries created in Apple Numbers, not official bank documents.", "official_url": "",
        "status": "secondary_lead_only", "recommended_action": "Use each summary only to locate an official rewards clause; never confirm an exclusion from the linked file alone.",
    },
    {
        "lead_id": "CC77-L012", "entity": "Multi-bank", "candidate_product": "Airport lounge and travel insurance fields",
        "lead_type": "schema_enrichment_candidate", "pdf_evidence": "Network comparison tables",
        "official_evidence": "Not validated bank-by-bank in this task.", "official_url": "",
        "status": "secondary_lead_only", "recommended_action": "Normalize provider, eligibility, visit allowance, guest rules, spend condition, and effective period after official confirmation.",
    },
    {
        "lead_id": "CC77-L013", "entity": "Multi-bank", "candidate_product": "Welcome, milestone, quarterly and annual bonuses",
        "lead_type": "schema_enrichment_candidate", "pdf_evidence": "Alfursan comparison table",
        "official_evidence": "Not validated bank-by-bank in this task.", "official_url": "",
        "status": "secondary_lead_only", "recommended_action": "Store each bonus as a separate event with spend threshold, window, recurrence, cap, and source date.",
    },
]


VAT_ROWS = [
    {
        "review_id": "CC77-VAT-001", "scope": "Generic international fee", "source_value": "2.30% shown in CC77",
        "comparison_value": "2.00% excluding VAT", "calculation": "2.00% x 1.15 = 2.30%",
        "classification": "plausible_vat_normalization", "decision": "Use as a reconciliation hypothesis only; confirm whether VAT legally applies to the exact fee and how the official source quotes it.",
    },
    {
        "review_id": "CC77-VAT-002", "scope": "Tweeq international fee", "source_value": "CC77 comparison context uses VAT-inclusive figures",
        "comparison_value": "Official Tweeq terms: 2.00% excluding VAT", "calculation": "2.00% x 1.15 = 2.30%",
        "classification": "official_basis_supports_hypothesis", "decision": "Stage 2.00% exclusive and 2.30% mathematical inclusive equivalent separately; do not overwrite any card value.",
    },
    {
        "review_id": "CC77-VAT-003", "scope": "urpay Visa international fee", "source_value": "CC77 digital-wallet table is visually ambiguous",
        "comparison_value": "Official urpay terms: 2.20% excluding VAT", "calculation": "2.20% x 1.15 = 2.53%",
        "classification": "potential_conflict_requires_validation", "decision": "Use the official terms as the current lead; keep the PDF value unparsed until card-column alignment is manually validated.",
    },
    {
        "review_id": "CC77-VAT-004", "scope": "ANB international fee conflict", "source_value": "CC77 commonly shows 2.30%",
        "comparison_value": "ANB tariff 2.00% versus product pages 2.75%", "calculation": "2.00% x 1.15 = 2.30%; this does not reconcile 2.75%",
        "classification": "conflict_not_resolved", "decision": "Preserve the existing official 2.00%/2.75% conflict. CC77 supports only a possible VAT interpretation of the tariff value.",
    },
    {
        "review_id": "CC77-VAT-005", "scope": "Annual fee normalization examples", "source_value": "CC77 includes 230, 345, 517.50, 862.50, 1,035 and 1,150 SAR",
        "comparison_value": "Possible pre-VAT bases: 200, 300, 450, 750, 900 and 1,000 SAR", "calculation": "base x 1.15 = displayed amount",
        "classification": "pattern_only_not_card_evidence", "decision": "Add explicit fee_vat_basis to future schema; never reverse-calculate a card fee without an official fee source.",
    },
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(name: str, rows) -> None:
    (MACHINE / name).write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_csv(name: str, rows: list[dict]) -> None:
    with (MACHINE / name).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    MACHINE.mkdir(parents=True, exist_ok=True)
    actual_hash = sha256(SOURCE)
    if actual_hash != EXPECTED_SHA256:
        raise SystemExit(f"Immutable source hash mismatch: {actual_hash}")

    reader = PdfReader(str(SOURCE))
    annotations = reader.pages[0].get("/Annots", []).get_object()
    urls = []
    for annotation in annotations:
        action = annotation.get_object().get("/A")
        action = action.get_object() if action else None
        if action and action.get("/URI"):
            urls.append(str(action.get("/URI")))
    drive_urls = [url for url in urls if "drive.google.com" in url]
    if len(drive_urls) != len(SUPPORTING_LINKS):
        raise SystemExit(f"Expected 13 supporting links, found {len(drive_urls)}")

    source_summary = {
        "source_id": "CC77-2026-08-15-V77",
        "path": str(SOURCE.relative_to(ROOT)),
        "sha256": actual_hash,
        "file_size_bytes": SOURCE.stat().st_size,
        "pages": len(reader.pages),
        "page_size_points": [float(reader.pages[0].mediabox.width), float(reader.pages[0].mediabox.height)],
        "displayed_version": 77,
        "displayed_update_date": "2026-08-15",
        "pdf_metadata": {str(k): str(v) for k, v in (reader.metadata or {}).items()},
        "source_type": "secondary_unverified_social_comparison",
        "authority_rank": 9,
        "publisher_identity": "credit_cards_sa / credit_cards23",
        "embedded_annotations": len(urls),
        "embedded_supporting_links": len(drive_urls),
        "extraction_date": EXTRACTED_ON,
        "master_data_changed": False,
    }
    write_json("cc77_source_summary.json", source_summary)

    link_rows = []
    for index, ((entity, title, linked_hash, linked_date), url) in enumerate(zip(SUPPORTING_LINKS, drive_urls), 1):
        link_rows.append({
            "link_id": f"CC77-LINK-{index:02d}", "entity": entity, "linked_document_title": title,
            "url": url, "linked_document_sha256_at_review": linked_hash, "linked_document_metadata_date": linked_date,
            "linked_document_creator": "Apple Numbers", "classification": "secondary_unverified_social_summary",
            "official_bank_document": "no", "stored_in_repository": "no",
            "reviewed_on": EXTRACTED_ON, "action": "Use only to locate and validate the applicable official rewards exclusion source.",
        })
    write_json("cc77_embedded_links.json", link_rows)
    write_csv("cc77_embedded_links.csv", link_rows)
    write_json("cc77_leads.json", LEADS)
    write_csv("cc77_leads.csv", LEADS)
    write_json("cc77_vat_review.json", VAT_ROWS)
    write_csv("cc77_vat_review.csv", VAT_ROWS)

    report = f"""# Credit Card Comparison Version 77 - Additive Ingestion Record

Generated: {EXTRACTED_ON}.

## Decision and safety boundary

`Credit Card 77_260818_125243.pdf` is preserved byte-for-byte as a secondary, unverified social-media comparison source. It is not an official bank publication and cannot confirm or overwrite a populated master value. Existing workbook sheets, card rows, card IDs, formulas, confidence classifications, and conflicts remain unchanged.

## Source identity

- Displayed version: 77.
- Displayed update date: 2026-08-15.
- SHA-256: `{actual_hash}`.
- PDF pages: {len(reader.pages)}; one unusually large comparison canvas.
- Publisher branding: `credit_cards_sa` / `credit_cards23`.
- Authority: rank 9, secondary/unverified source.
- Embedded annotations: {len(urls)}; supporting Google Drive documents: {len(drive_urls)}.

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
- Staged comparison leads: {len(LEADS)}.
- VAT review records: {len(VAT_ROWS)}.
- Embedded supporting-link records: {len(link_rows)}.
- Existing master rows overwritten: 0; deleted: 0; merged: 0.

## Required next work

Run separate identity-validation cycles for Tweeq and urpay before adding issuer or card IDs. For all other CC77 values, use the source only to locate current official tariffs, product pages, terms, and rewards documents. Never promote a CC77 value by itself.
"""
    REPORT.write_text(report, encoding="utf-8")
    print(json.dumps({"source_sha256": actual_hash, "embedded_links": len(link_rows), "leads": len(LEADS), "vat_rows": len(VAT_ROWS)}, indent=2))


if __name__ == "__main__":
    main()
