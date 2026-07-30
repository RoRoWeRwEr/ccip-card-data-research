---
schema_version: 1
repository: RoRoWeRwEr/ccip-card-data-research
purpose: Saudi payment-card research, consolidation, audit, and validation only
latest_origin_main_commit: 3de60260049687e9b26977f46e6d8b2254b21861
latest_completed_phase: "Phase 1 consolidation; Phase 2 ANB validation reviewed and awaiting PR #2 merge"
completed_banks:
  - name: Arab National Bank
    status: reviewed_with_evidence_gaps
    reviewed_products: 24
bank_currently_under_review: Arab National Bank
recommended_next_bank: Riyad Bank
open_pull_requests:
  - number: 2
    title: "Phase 2: validate ANB card portfolio"
    branch: codex/validate-anb-cards
    state: draft
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
exact_next_recommended_action: "Merge PR #2 after checks, then validate Riyad Bank from latest clean main using docs/prompts/BANK_VALIDATION_TASK.md."
last_updated_date: 2026-07-30
last_updated_commit: f073db98a39532b264522db84c601df850819459
---

# Project State

This repository is isolated from all CCIP application, migration, and database repositories. PR #1 consolidated the inherited research into `main`. The first Phase 2 bank cycle reviewed all 24 identifiable ANB products on branch `codex/validate-anb-cards`; Draft PR #2 is open.

ANB evidence gaps and official conflicts are preserved rather than resolved by inference. They do not block merging the additive audit register, but they prevent a claim of final complete ANB validation. Riyad Bank is the next recommended bank.

## Authoritative outputs

- `outputs/excel/saudi-credit-cards-unified-consolidated.xlsx`
- `outputs/MASTER_DATA_REFERENCE.md`
- `outputs/reports/`
- `outputs/machine-readable/`
- `docs/REPOSITORY_INVENTORY.md`
- `scripts/`

At task start, reconcile the YAML state above with `git`, GitHub, and the authoritative reports. At task end and before merge, update it without erasing historical state.
