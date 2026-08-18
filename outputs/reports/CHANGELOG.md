# Changelog

Generated: 2026-08-18.

## Inspected

- Repository source files: 56.
- Markdown files read: 11.
- Excel workbooks: 1; worksheets audited: 11.
- PDFs: 45; DOCX: 5; RTF: 1.

## Data changes

- Original master rows retained: 196; original row deletions: **0**.
- Original sheets retained: 11; original sheet deletions: **0**.
- Original populated values overwritten: **0**.
- Additive workbook sheets: **10** (six consolidation, one ANB validation, and three CC77 staging/provenance sheets).
- Chrome V4 guide records staged: 165; structured detail rows staged: 443.
- Exact-ID evidence links: 67.
- Unmatched/new-ID records preserved separately: 98.
- Field-level differences preserved as new conflict rows: 98.
- Inherited workbook conflicts preserved: 48.
- Missing-field observations: 74.
- Machine-readable card rows: 294.

## Intentionally unchanged

All original sheets, rows, cell values, formatting, formulas, comments, hyperlinks, and historical records. No identifier aliases were force-created for incompatible namespaces.

## Scripts and outputs

Created repeatable consolidation, validation, and comparison scripts. Generated the consolidated workbook, five machine-readable exports, repository inventory, master reference, audit, missing-data, conflict, collection-status, changelog, and final-validation plan.

## Credit Card comparison version 77 ingestion — 2026-08-18

- Preserved `Credit Card 77_260818_125243.pdf` unchanged at SHA-256 `8a51c97b8e1b3235f5799e05e41826d7ee7c420d1ef896af40691c4293f22902` and classified it as secondary/unverified evidence.
- Added three workbook sheets only: `CC77 Source Registry`, `CC77 Comparison Leads`, and `CC77 VAT Review`.
- Registered 13 embedded supporting links, 13 comparison leads, and 5 VAT-review records in new CSV/JSON outputs.
- Investigated Tweeq and urpay using current official terms; retained them as unmerged candidates with no new card IDs.
- Preserved the 146 existing conflict rows. No pre-existing card value, row, sheet, or identifier was changed, removed, or merged.

## Pre-merge release review

- Added the permanent repository separation, source-ingestion, and GitHub lifecycle policy to `AGENTS.md`.
- Removed the generated repository inventory from its own hash scope and excluded ignored runtime caches, eliminating recursive/non-source inventory drift.
- Added Git-backed raw-source preservation, generated-file placement, XLSX ZIP integrity, and Markdown UTF-8 checks.
- Added `scripts/check_reproducibility.py`; two independent rebuilds produced identical deterministic reports/exports and identical workbook semantics.
- Normalized generated CSV line endings to LF so repository diffs are stable across environments.
