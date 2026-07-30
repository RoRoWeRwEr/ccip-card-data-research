#!/usr/bin/env python3
"""Render a stable GitHub Issue/PR body from the latest monitoring report."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
report = json.loads((ROOT / "monitoring/changes/latest.json").read_text(encoding="utf-8"))
lines = ["<!-- bank-card-monitor -->", "# Bank-card source changes", "", f'Checked: `{report["checked_at"]}`', "", "Monitoring detected official-source changes. The authoritative Excel was not modified.", "", "| Bank | Source | Types | Before | After |", "| --- | --- | --- | --- | --- |"]
for event in report["changes"]:
    before, after = event.get("before") or {}, event.get("after") or {}
    lines.append(f'| {event["bank_name"]} | {event["source_label"]} | {", ".join(event["change_types"])} | `{str(before.get("content_sha256", ""))[:12]}` / {before.get("status_code")} | `{str(after.get("content_sha256", ""))[:12]}` / {after.get("status_code")} |')
lines += ["", "## Required next action", "", "Run the dispatched full bank-validation workflow, review official evidence, and add evidence through the repository’s non-destructive process. Do not update the workbook from monitoring evidence alone."]
(ROOT / "monitoring/runs/notice.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
