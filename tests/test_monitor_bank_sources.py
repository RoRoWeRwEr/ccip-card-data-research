import importlib.util
import http.client
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("monitor", Path(__file__).parents[1] / "scripts/monitor_bank_sources.py")
monitor = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(monitor)


class MonitorTests(unittest.TestCase):
    def test_incomplete_read_is_retryable(self):
        self.assertTrue(issubclass(http.client.IncompleteRead, http.client.HTTPException))

    def test_html_normalization_ignores_scripts_and_whitespace(self):
        first = monitor.normalize_html(b"<html><script>x=1</script><body>A   card</body></html>")
        second = monitor.normalize_html(b"<body>A card</body>")
        self.assertEqual(first, second)

    def test_detects_changed_and_inaccessible(self):
        bank = {"id": "riyad-bank", "name": "Riyad Bank"}
        old = {"requested_url": "https://example.test/a", "label": "Cards", "accessible": True, "content_sha256": "old", "content_text": "old", "status_code": 200}
        current = {"source_id": "cards", "kind": "card_catalog", "label": "Cards", "requested_url": "https://example.test/a", "material": True, "checked_at": "2026-07-30T00:00:00Z", "accessible": False, "content_sha256": "", "content_text": "", "status_code": 503, "final_url": "https://example.test/a", "etag": "", "last_modified": "", "content_length": 0, "raw_sha256": "", "error": "HTTPError"}
        event = monitor.diff_record(bank, current, old)
        self.assertEqual(event["change_types"], ["inaccessible"])

    def test_detects_new_source(self):
        bank = {"id": "riyad-bank", "name": "Riyad Bank"}
        current = {"source_id": "new-card", "kind": "card_catalog", "label": "New Card", "requested_url": "https://example.test/new", "material": True, "checked_at": "2026-07-30T00:00:00Z", "accessible": True, "content_sha256": "new", "content_text": "new", "status_code": 200, "final_url": "https://example.test/new", "etag": "", "last_modified": "", "content_length": 3, "raw_sha256": "new", "error": ""}
        event = monitor.diff_record(bank, current, None)
        self.assertEqual(event["change_types"], ["new"])

    def test_registry_ids_and_source_ids_are_unique(self):
        registry = json.loads((Path(__file__).parents[1] / "monitoring/registry/banks.json").read_text())
        ids = [row["id"] for row in registry["institutions"]]
        self.assertEqual(len(ids), len(set(ids)))
        riyad = next(row for row in registry["institutions"] if row["id"] == "riyad-bank")
        source_ids = [row["id"] for row in riyad["sources"]]
        self.assertEqual(len(source_ids), len(set(source_ids)))
        self.assertEqual({row["kind"] for row in riyad["sources"]}, {"card_catalog", "pricing_guide", "terms_and_conditions", "rewards_page", "rewards_terms"})


if __name__ == "__main__":
    unittest.main()
