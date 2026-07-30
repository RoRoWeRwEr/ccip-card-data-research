#!/usr/bin/env python3
"""Fetch registered official sources and emit non-destructive change records."""

from __future__ import annotations

import argparse
import difflib
import hashlib
import html
import json
import re
import ssl
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "monitoring/registry/banks.json"
STATE = ROOT / "monitoring/state/latest.json"
LATEST_RUN = ROOT / "monitoring/runs/latest.json"
LATEST_CHANGES = ROOT / "monitoring/changes/latest.json"
EVENT_LOG = ROOT / "monitoring/changes/events.jsonl"
USER_AGENT = "ccip-card-data-research-monitor/1.0 (+https://github.com/RoRoWeRwEr/ccip-card-data-research)"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def normalize_html(raw: bytes) -> str:
    text = raw.decode("utf-8", errors="replace")
    text = re.sub(r"(?is)<(script|style|noscript|svg).*?</\1>", " ", text)
    text = re.sub(r"(?is)<!--.*?-->", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def fetch(source: dict[str, Any], timeout: int, retries: int) -> dict[str, Any]:
    requested_url = source["url"]
    result: dict[str, Any] = {
        "source_id": source["id"], "kind": source["kind"], "label": source["label"],
        "requested_url": requested_url, "material": bool(source.get("material", True)),
        "checked_at": utc_now(), "accessible": False, "status_code": None, "final_url": requested_url,
        "content_type": "", "etag": "", "last_modified": "", "content_length": 0,
        "raw_sha256": "", "content_sha256": "", "content_text": "", "error": "",
    }
    request = urllib.request.Request(requested_url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/pdf,*/*;q=0.8"})
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout, context=ssl.create_default_context()) as response:
                raw = response.read()
                result.update({
                    "accessible": 200 <= response.status < 400, "status_code": response.status,
                    "final_url": response.geturl(), "content_type": response.headers.get_content_type(),
                    "etag": response.headers.get("ETag", ""), "last_modified": response.headers.get("Last-Modified", ""),
                    "content_length": len(raw), "raw_sha256": hashlib.sha256(raw).hexdigest(),
                    "error": "",
                })
                normalized = normalize_html(raw) if result["content_type"] in {"text/html", "application/xhtml+xml"} else ""
                result["content_text"] = normalized
                canonical = normalized.encode("utf-8") if normalized else raw
                result["content_sha256"] = hashlib.sha256(canonical).hexdigest()
                return result
        except urllib.error.HTTPError as exc:
            result.update({"status_code": exc.code, "final_url": exc.geturl(), "error": f"HTTPError: {exc.code} {exc.reason}"})
        except (urllib.error.URLError, TimeoutError, ssl.SSLError, ConnectionError, OSError) as exc:
            result["error"] = f"{type(exc).__name__}: {exc}"
        if attempt < retries:
            time.sleep(2 ** attempt)
    return result


def diff_record(bank: dict[str, Any], current: dict[str, Any], previous: dict[str, Any] | None) -> dict[str, Any] | None:
    if previous is None:
        return {
            "event_id": hashlib.sha256(f'{bank["id"]}:{current["source_id"]}:new:{current["content_sha256"]}'.encode()).hexdigest()[:20],
            "detected_at": current["checked_at"], "bank_id": bank["id"], "bank_name": bank["name"],
            "source_id": current["source_id"], "source_kind": current["kind"], "source_label": current["label"],
            "change_types": ["new"], "material": current["material"], "similarity_ratio": None,
            "before": None,
            "after": {key: current.get(key) for key in ["requested_url", "final_url", "status_code", "accessible", "etag", "last_modified", "content_length", "raw_sha256", "content_sha256", "error"]},
        }
    types: list[str] = []
    if current["requested_url"] != previous.get("requested_url") or current["label"] != previous.get("label"):
        types.append("renamed")
    if previous.get("accessible") and not current["accessible"]:
        types.append("inaccessible")
    elif not previous.get("accessible") and current["accessible"]:
        types.append("restored")
    if current["accessible"] and previous.get("accessible") and current["content_sha256"] != previous.get("content_sha256"):
        types.append("changed")
    if not types:
        return None
    old_text, new_text = previous.get("content_text", ""), current.get("content_text", "")
    similarity = round(difflib.SequenceMatcher(None, old_text, new_text).ratio(), 4) if old_text or new_text else None
    return {
        "event_id": hashlib.sha256(f'{bank["id"]}:{current["source_id"]}:{previous.get("content_sha256", "")}:{current["content_sha256"]}'.encode()).hexdigest()[:20],
        "detected_at": current["checked_at"], "bank_id": bank["id"], "bank_name": bank["name"],
        "source_id": current["source_id"], "source_kind": current["kind"], "source_label": current["label"],
        "change_types": types, "material": current["material"], "similarity_ratio": similarity,
        "before": {key: previous.get(key) for key in ["requested_url", "final_url", "status_code", "accessible", "etag", "last_modified", "content_length", "raw_sha256", "content_sha256"]},
        "after": {key: current.get(key) for key in ["requested_url", "final_url", "status_code", "accessible", "etag", "last_modified", "content_length", "raw_sha256", "content_sha256", "error"]},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", help="Monitor one bank id; default is every active bank")
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--retries", type=int, default=2)
    args = parser.parse_args()
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    is_baseline = not STATE.exists()
    previous_state = json.loads(STATE.read_text(encoding="utf-8")) if not is_baseline else {"sources": {}}
    previous = previous_state.get("sources", {})
    banks = [b for b in registry["institutions"] if b["monitoring_status"] == "active" and (not args.bank or b["id"] == args.bank)]
    if args.bank and not banks:
        raise SystemExit(f"No active bank found for {args.bank!r}")
    current_sources: dict[str, Any] = {}
    changes: list[dict[str, Any]] = []
    current_ids: set[str] = set()
    for bank in banks:
        for source in bank["sources"]:
            key = f'{bank["id"]}/{source["id"]}'
            current_ids.add(key)
            observation = fetch(source, args.timeout, args.retries)
            observation.update({"bank_id": bank["id"], "bank_name": bank["name"]})
            current_sources[key] = observation
            event = None if is_baseline else diff_record(bank, observation, previous.get(key))
            if event:
                changes.append(event)
    for key, old in previous.items():
        if key not in current_ids and (not args.bank or old.get("bank_id") == args.bank):
            changes.append({
                "event_id": hashlib.sha256(f'{key}:removed:{old.get("content_sha256", "")}'.encode()).hexdigest()[:20],
                "detected_at": utc_now(), "bank_id": old.get("bank_id"), "bank_name": old.get("bank_name"),
                "source_id": old.get("source_id"), "source_kind": old.get("kind"), "source_label": old.get("label"),
                "change_types": ["removed"], "material": bool(old.get("material", True)), "similarity_ratio": None,
                "before": old, "after": None,
            })
    combined = dict(previous)
    combined.update(current_sources)
    for key in list(combined):
        if key not in current_ids and (not args.bank or combined[key].get("bank_id") == args.bank):
            del combined[key]
    material = [event for event in changes if event["material"]]
    checked_at = utc_now()
    state = {"schema_version": 1, "checked_at": checked_at, "registry_sha256": hashlib.sha256(REGISTRY.read_bytes()).hexdigest(), "sources": combined}
    report = {"schema_version": 1, "checked_at": checked_at, "baseline_created": is_baseline, "banks_checked": [b["id"] for b in banks], "source_count": len(current_sources), "change_count": len(changes), "material_change_count": len(material), "changes": changes}
    for path, payload in [(STATE, state), (LATEST_RUN, report), (LATEST_CHANGES, report)]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if changes:
        EVENT_LOG.parent.mkdir(parents=True, exist_ok=True)
        existing_ids = set()
        if EVENT_LOG.exists():
            for line in EVENT_LOG.read_text(encoding="utf-8").splitlines():
                if line.strip(): existing_ids.add(json.loads(line)["event_id"])
        with EVENT_LOG.open("a", encoding="utf-8") as handle:
            for event in changes:
                if event["event_id"] not in existing_ids:
                    handle.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
    print(json.dumps({key: report[key] for key in ["checked_at", "baseline_created", "banks_checked", "source_count", "change_count", "material_change_count"]}))


if __name__ == "__main__":
    main()
