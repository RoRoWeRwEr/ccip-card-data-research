# Continuous bank-card monitoring

The monitoring system watches official public sources for Saudi payment-card research. It is an early-warning system, not an evidence-ingestion or workbook-editing system. Riyad Bank is the first active bank; every issuer in the current research dataset has a registry entry so coverage can expand without changing the engine.

## What runs automatically

GitHub Actions runs every Monday and Thursday at 06:17 Asia/Riyadh (03:17 UTC), or on demand. It downloads each active source, records HTTP and document metadata, hashes raw and normalized content, and compares the result with the last committed observation.

The detector classifies `changed`, `renamed`, `removed`, `inaccessible`, and `restored` sources. The first successful run establishes a baseline and does not create an alert. Later material changes update `monitoring/changes/latest.json` and the append-only `events.jsonl`. An automated branch, Draft PR, and tracking Issue are created or updated. A repository-dispatch event then starts the full bank-validation request workflow.

The monitor never runs `scripts/consolidate.py`, `scripts/validate_anb_phase2.py`, or any workbook writer. The authoritative Excel cannot be changed by either monitoring workflow.

## Your role

1. Review the tracking Issue and Draft PR when GitHub notifies you.
2. Provide a business decision only if official evidence remains materially conflicting, a destructive identity merge is proposed, or a required document is inaccessible.
3. Approve the reviewed validation PR when evidence and repository checks are complete.

You do not need to download reports, create branches, or copy data between tools.

## The agent's role

1. Start from `PROJECT_STATE.md` and the detected machine-readable change report.
2. Apply `docs/prompts/BANK_VALIDATION_TASK.md` only for the affected bank.
3. Compare the changed official source with the current tariff, terms, product pages, and rewards rules.
4. Preserve conflicts and provenance, update the validation register and reports additively, run all repository checks, and manage the PR lifecycle.
5. Modify the consolidated workbook only during that reviewed full-validation task—never directly from the monitoring result.

## Add the next bank

1. Verify its official domain and URLs for card catalog, pricing, card terms, and rewards.
2. Add those sources to the existing institution in `monitoring/registry/banks.json` and set `monitoring_status` to `active`.
3. Run `python3 scripts/monitor_bank_sources.py --bank <bank-id>` once to establish its baseline.
4. Run `python3 -m unittest discover -s tests -v` and `python3 scripts/validate_outputs.py`.
5. Publish the baseline through the normal reviewed GitHub lifecycle.

## Manual operation

Run all active banks:

```bash
python3 scripts/monitor_bank_sources.py
```

Run Riyad Bank only:

```bash
python3 scripts/monitor_bank_sources.py --bank riyad-bank
```

Inspect `monitoring/runs/latest.json` for the run summary and `monitoring/changes/latest.json` for detected events. Failed URLs are recorded rather than silently discarded.
