# Standard Bank Validation Task

## Minimal user input

```text
Bank: <bank name>
Official website: <URL>
```

The two lines above authorize the complete workflow below for one bank only. Do not request a longer prompt.

## Mandatory execution workflow

1. Verify the repository is exactly `RoRoWeRwEr/ccip-card-data-research`; never touch a CCIP application, migration, database, or other repository.
2. Read, completely and in order: `AGENTS.md`, `PROJECT_STATE.md`, `outputs/MASTER_DATA_REFERENCE.md`, collection status, changelog, conflicts, and missing-information reports.
3. Fetch `origin/main`, verify latest clean `main`, then create a task branch. If explicitly continuing an active PR, synchronize and use its existing branch.
4. Inspect all existing research for the named bank: immutable PDFs, terms, pricing guides, product guides, DOCX/RTF files, Claude/ChatGPT research, every relevant Excel worksheet, Markdown report, source registry, conflict, and machine-readable record. Continue from existing work.
5. Inventory every identifiable current, new, renamed, replaced, unavailable, uncertain, historical, and discontinued product, including credit, charge, prepaid, low-limit, multi-currency, mada/debit, payroll, business, corporate, purchasing, supplementary, and virtual cards.
6. Use final evidence only from official bank, regulator, airline/reward partner, or payment-network sources as applicable. Review the official website, current pricing/tariff, product T&C, generic card T&C, reward rules, FAQs, and product-status evidence. Record the exact URL, document/effective date when available, retrieval date, and applicability.
7. Validate for every card: identity, Arabic/English name, issuer, network, type/tier, current status, eligibility, annual/supplementary/replacement fees, APR or purchase rate, FX/international fees, cash withdrawal/transfer fees and limits, minimum payment, rewards and category caps, welcome/renewal bonuses, lounge access, insurance, benefits, credit/load limits, and exclusions.
8. Preserve every conflicting official value with its source and date. Never silently overwrite a populated Excel value, delete a card, or force an uncertain identity merge.
9. Apply safe additive Excel changes automatically with provenance. Add missing data only when identity and applicability are defensible. Ask the user only for an irreversible merge, deletion, subjective classification, unreliable material source, or unresolved conflict that must be reduced to one value.
10. Update the consolidated Excel, `outputs/MASTER_DATA_REFERENCE.md`, `PROJECT_STATE.md`, repository inventory when sources changed, collection status, conflicts, missing information, changelog, source/provenance records, and machine-readable exports where lossless and safe.
11. Preserve raw sources byte-for-byte. Store any newly acquired official document in the existing raw source folder without replacing another file, then update inventory and hashes.
12. Add or update repeatable scripts when useful. Scripts must never mutate raw sources.
13. Run workbook-open/ZIP checks, original-sheet/row/formula preservation checks, raw-source hash checks, CSV/JSON syntax checks, report consistency, workbook rendering, comparisons, and reproducibility checks. Fix failures.
14. Commit all scoped work, push the task branch, and create or update its pull request. Keep the PR description and checks current.
15. When the bank phase is cohesive, checks pass, and no material user decision blocks the changes, mark the PR ready, merge it into `main`, verify `main`, and delete the completed branch when safe.
16. Update `PROJECT_STATE.md` with completion status, remaining evidence gaps, open decisions, merge state, and the next recommended bank.

Never claim final bank validation while a required official source is missing or an unresolved conflict remains. A missing document blocks only the affected bank or fields; document it precisely and complete all unaffected work.
