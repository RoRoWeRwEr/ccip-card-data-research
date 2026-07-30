---
schema_version: 1
repository: RoRoWeRwEr/ccip-card-data-research
purpose: Saudi payment-card research, consolidation, audit, and validation only
latest_origin_main_commit: 36dbefebb2cb4208062ad7c73f1df3630b043be9
latest_completed_phase: "Phase 2 ANB validation and permanent autonomous repository operating system"
completed_banks:
  - name: Arab National Bank
    status: reviewed_with_evidence_gaps
    reviewed_products: 24
bank_currently_under_review: null
recommended_next_bank: Riyad Bank
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
exact_next_recommended_action: "Validate Riyad Bank from latest clean main using docs/prompts/BANK_VALIDATION_TASK.md."
last_updated_date: 2026-07-30
last_updated_commit: 36dbefebb2cb4208062ad7c73f1df3630b043be9
---

# Project State

This repository is isolated from all CCIP application, migration, and database repositories. PR #1 consolidated the inherited research into `main`. PR #2 merged the first Phase 2 bank cycle, covering all 24 identifiable ANB products, together with the permanent autonomous repository operating system.

ANB evidence gaps and official conflicts are preserved rather than resolved by inference. They do not block merging the additive audit register, but they prevent a claim of final complete ANB validation. Riyad Bank is the next recommended bank.

## Authoritative outputs

- `outputs/excel/saudi-credit-cards-unified-consolidated.xlsx`
- `outputs/MASTER_DATA_REFERENCE.md`
- `outputs/reports/`
- `outputs/machine-readable/`
- `docs/REPOSITORY_INVENTORY.md`
- `scripts/`

At task start, reconcile the YAML state above with `git`, GitHub, and the authoritative reports. At task end and before merge, update it without erasing historical state.
