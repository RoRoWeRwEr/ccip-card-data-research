# Automation

Use the bundled Python runtime when available:

```bash
PYTHON=/Users/rayanmaghrabi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3
$PYTHON scripts/consolidate.py
$PYTHON scripts/validate_outputs.py
$PYTHON scripts/compare_workbooks.py
$PYTHON scripts/check_reproducibility.py
```

The scripts read immutable files under `Credit Cards Terms and Conditions/` and write only to `working/`, `docs/`, and `outputs/`. They are designed to be rerunnable. The workbook comparison is semantic because XLSX ZIP timestamps can change between runs.

Official-source monitoring is separate and never writes the workbook:

```bash
python3 scripts/monitor_bank_sources.py --bank riyad-bank
python3 -m unittest discover -s tests -v
```

See `docs/monitoring/README.md` for the scheduled workflow, alert lifecycle, and role split.
