# Automation

Use the bundled Python runtime when available:

```bash
PYTHON=/Users/rayanmaghrabi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3
$PYTHON scripts/consolidate.py
$PYTHON scripts/validate_outputs.py
$PYTHON scripts/compare_workbooks.py
```

The scripts read immutable files under `Credit Cards Terms and Conditions/` and write only to `working/`, `docs/`, and `outputs/`. They are designed to be rerunnable. The workbook comparison is semantic because XLSX ZIP timestamps can change between runs.
