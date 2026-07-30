# Standard New-Source Ingestion Task

## Minimal user input

```text
Process all new repository source files according to AGENTS.md.
```

This line authorizes the complete source-ingestion workflow below.

## Mandatory execution workflow

1. Perform the mandatory bootstrap and ordered reading sequence in `AGENTS.md`. Verify the exact repository, latest clean `origin/main`, authoritative outputs, and `PROJECT_STATE.md`.
2. Create a task branch. Compare the current raw-source tree with the committed inventory and hash snapshot to detect every new, modified, missing, renamed, or suspected duplicate file.
3. Preserve raw files byte-for-byte. Never edit, overwrite, rename, destructively move, or delete an uploaded PDF, pricing guide, T&C, DOCX, RTF, Markdown research file, workbook, or other source.
4. Identify each document's bank/issuer, applicable products, document class, language, publication/effective date, source URL when known, extractability, and relationship to existing sources.
5. Extract usable evidence with appropriate PDF/document/spreadsheet tooling, including visual review for layout-dependent tables. Record extraction limitations.
6. Compare every material item against the consolidated Excel, master reference, provenance records, conflicts, missing-information backlog, collection status, and machine-readable exports.
7. Classify each finding as new card, safe missing-data addition, correction candidate, current/historical/discontinued status, duplicate source, conflict, missing evidence, inference, or no-op confirmation.
8. Apply safe additive updates automatically with explicit provenance. Never silently overwrite populated Excel values or merge/delete records. Request user approval only for destructive, irreversible, subjective, or materially uncertain changes.
9. Update source hashes and inventory, consolidated Excel, master reference, `PROJECT_STATE.md`, collection status, conflicts, missing information, changelog, provenance/sources, and safe machine-readable exports.
10. Add repeatable ingestion or validation automation when useful. Never let scripts modify raw inputs.
11. Run raw-hash preservation, workbook structure/formula/row, export syntax, report consistency, rendering, comparison, and reproducibility validations; fix failures.
12. Commit and push the task branch, create or update its pull request, keep the PR description current, and fix CI/check failures.
13. When the ingestion phase is complete, checks pass, and no material decision remains, mark the PR ready, merge into `main`, verify main contains all outputs, delete the branch when safe, and update `PROJECT_STATE.md` with the exact next action.

If a source is encrypted, corrupt, unsupported, inaccessible, or materially unreliable, identify the exact file and error. Continue processing every unaffected source.
