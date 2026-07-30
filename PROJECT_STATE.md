---
schema_version: 1
repository: RoRoWeRwEr/ccip-card-data-research
purpose: Saudi payment-card research, consolidation, audit, and validation only
latest_origin_main_commit: 6a8458e62d5dd415db7cbeec8be761c0dc212607
latest_completed_phase: "Continuous bank-card monitoring system with Riyad Bank baseline"
completed_banks:
  - name: Arab National Bank
    status: reviewed_with_evidence_gaps
    reviewed_products: 24
bank_currently_under_review: null
recommended_next_bank: Riyad Bank
monitoring:
  status: active_baseline_established
  schedule: "Mondays and Thursdays at 03:17 UTC (06:17 Asia/Riyadh)"
  registered_institutions: 19
  active_banks:
    - Riyad Bank
  active_sources: 5
  last_baseline_result: "All five official sources accessible; no authoritative Excel changes."
  validation_trigger: "Only a detected material source change dispatches full bank validation."
open_pull_requests: []
pending_user_decisions:
  - "Approval required before any irreversible ANB-01 to ANB-19 identifier remap or record merge."
  - "Selection required only if one international-fee value must be forced before ANB resolves 2% tariff versus 2.75% product-page evidence."
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
exact_next_recommended_action: "Let the scheduled Riyad Bank monitor run; when it detects a material change, complete the dispatched full validation before any evidence-driven workbook update. Then onboard Al Rajhi Bank as the next monitored bank."
last_updated_date: 2026-07-30
last_updated_commit: pending-monitoring-system-commit
---

# Project State

This repository is isolated from all CCIP application, migration, and database repositories. PR #1 consolidated the inherited research into `main`. PR #2 merged the first Phase 2 bank cycle, covering all 24 identifiable ANB products, together with the permanent autonomous repository operating system. PR #3 finalized the post-merge state. The current task adds continuous official-source monitoring with Riyad Bank as the first active bank.

ANB evidence gaps and official conflicts are preserved rather than resolved by inference. They do not block merging the additive audit register, but they prevent a claim of final complete ANB validation. Riyad Bank is the next recommended bank.

The monitoring baseline covers Riyad Bank's official card catalog, fee disclosure, card terms, rewards page, and rewards terms. Monitoring records hashes, metadata, accessibility, and content comparisons in machine-readable files. It never modifies the authoritative or consolidated Excel automatically. A material change opens or updates a tracking Issue and Draft PR, then dispatches the full bank-validation workflow.

## Authoritative outputs

- `outputs/excel/saudi-credit-cards-unified-consolidated.xlsx`
- `outputs/MASTER_DATA_REFERENCE.md`
- `outputs/reports/`
- `outputs/machine-readable/`
- `docs/REPOSITORY_INVENTORY.md`
- `scripts/`

At task start, reconcile the YAML state above with `git`, GitHub, and the authoritative reports. At task end and before merge, update it without erasing historical state.
