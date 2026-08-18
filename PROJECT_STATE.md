---
schema_version: 1
repository: RoRoWeRwEr/ccip-card-data-research
purpose: Saudi payment-card research, consolidation, audit, and validation only
latest_origin_main_commit: 819c6f1f3fad59b3fb3107a8f781d1ee57394f9e
latest_completed_phase: "Additive CC77 secondary-source ingestion and Tweeq/urpay lead staging"
completed_banks:
  - name: Arab National Bank
    status: reviewed_with_evidence_gaps
    reviewed_products: 24
bank_currently_under_review: null
recommended_next_bank: Riyad Bank
monitoring:
  status: material_change_detected_validation_triggered
  schedule: "Mondays and Thursdays at 03:17 UTC (06:17 Asia/Riyadh)"
  registered_institutions: 19
  active_banks:
    - Riyad Bank
  active_sources: 5
  last_baseline_result: "Riyad card-fee PDF was inaccessible from the GitHub-hosted runner after retries; Issue #7 records the event. Local baseline remains preserved and the authoritative Excel was not changed."
  validation_trigger: "Only a detected material source change dispatches full bank validation."
  active_change_issue: "https://github.com/RoRoWeRwEr/ccip-card-data-research/issues/7"
  validation_dispatch_run: "https://github.com/RoRoWeRwEr/ccip-card-data-research/actions/runs/30529341372"
open_pull_requests: []
pending_user_decisions:
  - "Approval required before any irreversible ANB-01 to ANB-19 identifier remap or record merge."
  - "Selection required only if one international-fee value must be forced before ANB resolves 2% tariff versus 2.75% product-page evidence."
  - "No CC77 decision is required now because Tweeq, urpay, linked summaries, and VAT interpretations remain unmerged staging records."
missing_source_documents:
  - "ANB World Elite Select current product, pricing, and rewards disclosure."
  - "ANB World Elite Exclusive disclosure explicitly attributing the SAR 3,000 fee."
  - "ANB mada Infinite, Platinum, Gold, and Classic tier pricing and unambiguous 250-point formula."
  - "ANB Corporate, Business, and Purchase Card pricing and rewards-applicability schedule."
  - "ANB Visa Classic current product page or formal status confirmation."
outstanding_conflicts:
  - "ANB international transaction fee: 2% tariff versus 2.75% individual product pages."
  - "ANB premium international earning: 1.8 versus 2.2 points per SAR in official reward files."
  - "ANB inherited identifiers ANB-01 to ANB-19 map to different historical and Chrome V4 product names."
exact_next_recommended_action: "Open a new task to validate Tweeq and urpay identities and current product availability against dated official sources before assigning any issuer/card IDs; keep Riyad Bank Issue #7 active as the existing monitoring follow-up."
last_updated_date: 2026-08-18
last_updated_commit: 819c6f1f3fad59b3fb3107a8f781d1ee57394f9e
---

# Project State

This repository is isolated from all CCIP application, migration, and database repositories. PR #1 consolidated the inherited research into `main`. PR #2 merged the first Phase 2 bank cycle, covering all 24 identifiable ANB products, together with the permanent autonomous repository operating system. PR #3 finalized the post-merge state. The current task adds continuous official-source monitoring with Riyad Bank as the first active bank.

ANB evidence gaps and official conflicts are preserved rather than resolved by inference. They do not block merging the additive audit register, but they prevent a claim of final complete ANB validation. Riyad Bank is the next recommended bank.

PR #4 squash-merged the monitoring system to `main` as `877b5aa90275ebaa95a9f250808dfe83014dbd40`; PRs #6 and #8 hardened runner transport and repository-setting fallbacks. The monitoring baseline covers Riyad Bank's official card catalog, fee disclosure, card terms, rewards page, and rewards terms. Monitoring records hashes, metadata, accessibility, and content comparisons in machine-readable files. It never modifies the authoritative or consolidated Excel automatically.

The first GitHub-hosted smoke run detected that the Riyad card-fee PDF was inaccessible after retries, created Issue #7, and preserved the machine-readable evidence on `monitoring/automated-updates`. The change-only full-validation dispatch completed successfully. This is an accessibility alert, not evidence that the source was removed and not authority to alter the workbook.

The 2026-08-18 CC77 task preserved `Credit Card 77_260818_125243.pdf` unchanged as an authority-rank-9 secondary source. It added three staging/provenance workbook sheets, 13 embedded-link records, 13 comparison leads, and 5 VAT-review records. Tweeq and urpay were checked against current official terms but remain unmerged candidates. Existing master rows, identifiers, conflicts, and populated values were not changed.

## Authoritative outputs

- `outputs/excel/saudi-credit-cards-unified-consolidated.xlsx`
- `outputs/MASTER_DATA_REFERENCE.md`
- `outputs/reports/`
- `outputs/machine-readable/`
- `docs/REPOSITORY_INVENTORY.md`
- `scripts/`

At task start, reconcile the YAML state above with `git`, GitHub, and the authoritative reports. At task end and before merge, update it without erasing historical state.
