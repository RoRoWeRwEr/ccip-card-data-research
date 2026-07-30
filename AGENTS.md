# Saudi Payment Cards Research - Operating Manual

## Purpose and scope

This repository consolidates research about Saudi Arabian credit, charge, prepaid, low-limit, multi-currency, payroll, and mada/debit cards. It is a research and data-governance repository only. Do not integrate its data into the main CCIP platform, `index.html`, `CARD_DB`, or another production database from this repository.

The current objective is a traceable working dataset. It is not proof that every product is current or finally validated.

## Protected source material

Treat every file in `Credit Cards Terms and Conditions/` as an immutable source. In particular:

- `01. saudi-credit-cards-unified V3.xlsx` is the original Excel master.
- `02. Xlsx audit master reference 2026 07 29.md` is the authoritative continuation reference for inherited methodology and decisions.
- `03. Cards information from Claude Chrome prompt V4.md` is newer official-site research, but it is incomplete and contains identifier schemes that do not always match the master.
- The remaining PDFs, DOCX files, and RTF file are official or supporting bank documents.

Never overwrite, delete, rename, or destructively move a source. Work in `working/`; publish deliverables in `outputs/`.

## Source priority

Use this provisional hierarchy during consolidation:

1. Current official pricing guide or tariff.
2. Official product terms and conditions.
3. Current official bank product page.
4. Official rewards or benefits terms.
5. Official FAQ or campaign material.
6. Official payment-network source.
7. Prior Claude/ChatGPT research with a traceable official source.
8. Existing workbook value without traceable support.
9. Secondary or unverified source.

This hierarchy does not permit silent overwrites. If official sources conflict, preserve every value, source, and date and create a conflict record.

## Non-deletion and identity policy

- Never delete a card or historical record because it appears duplicated, replaced, discontinued, incomplete, or out of date.
- Preserve current, historical, discontinued, replaced, uncertain, and excluded records.
- Do not permanently merge records unless identity is supported by multiple attributes: issuer, Arabic/English name, network, tier, product type, fees, rewards, URL/document, and status.
- A matching `card_id` is safe for provisional reconciliation but does not justify overwriting a conflicting populated field.
- Different ID namespaces such as `AJB`/`ALJAZIRA`, `RYB`/`RIYAD`, or `ARB`/Rajhi identifiers remain unresolved until mapped explicitly.
- Historical exclusions inherited from the prior reference (BSF-13, BSF-14, ALJAZIRA-04) remain documented; do not erase their history.

## Evidence model

Every material value must be classifiable as one of:

- `direct`: stated by an identified source.
- `normalized`: formatting or terminology normalized without changing meaning.
- `inferred`: derived from evidence and explicitly marked as inference.
- `conflict`: two or more incompatible values are preserved.
- `missing`: expected but not located.
- `provisional`: working decision pending final validation.
- `confirmed`: decision supported by applicable evidence; final confirmation is reserved for the later validation phase.

Record source file or URL, source type, source date when available, extraction date, and notes. `calcTier` retains its inherited meanings: `precise`, `estimated`, and `unavailable`.

## Excel rules

- Never overwrite the original workbook.
- Preserve all original sheets, records, cell values, formatting, filters, tables, comments, formulas, hyperlinks, validations, merges, hidden states, and freeze panes unless a repair is necessary and documented.
- Prefer additive sheets and columns. Do not flatten the workbook merely to simplify automation.
- Only fill a blank master field automatically when an exact `card_id` match supplies a compatible value. Record every such addition.
- Never overwrite a populated conflict. Put both values in the reconciliation/conflict records.
- Keep source URLs as plain text and preserve Arabic text.
- Validate that the output opens, all original sheet names remain, formulas are preserved, original row counts do not decrease, and deletion count is zero.

## Workflow for future agents

1. Read this file and `outputs/MASTER_DATA_REFERENCE.md` before processing.
2. Confirm the repository, branch, and clean/dirty state. Preserve unrelated user changes.
3. Hash and inventory sources before processing.
4. Run `scripts/consolidate.py` to rebuild reports, exports, and the consolidated workbook from immutable sources.
5. Run `scripts/validate_outputs.py` and `scripts/compare_workbooks.py`.
6. Review `outputs/reports/CONFLICTS_AND_DECISIONS.md` and `MISSING_INFORMATION.md` before making new decisions.
7. Add new evidence rather than replacing old evidence. Update the consolidated master reference and changelog with counts.
8. For final validation, check every identifiable card against current official product pages, current tariffs, T&Cs, and rewards terms. Only then promote provisional decisions to final confirmed decisions.

## Expected outputs

- `outputs/excel/saudi-credit-cards-unified-consolidated.xlsx`
- `outputs/MASTER_DATA_REFERENCE.md`
- reports under `outputs/reports/`
- machine-readable CSV/JSON exports under `outputs/machine-readable/`
- repository inventory at `docs/REPOSITORY_INVENTORY.md`

## When to consult the user

Ask only for a material business decision: an uncertain irreversible merge, any deletion, a major workbook redesign, a subjective field interpretation, an unreliable source that materially changes data, an unresolved material official-source conflict requiring selection, or a missing business rule. Group related questions and continue unaffected work.

Do not ask for approval for safe formatting, additive evidence records, report generation, or other reversible technical decisions.
