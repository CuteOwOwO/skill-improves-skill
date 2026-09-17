#!/usr/bin/env python3
"""Deterministically grade minimal-change-router JSON answers."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


FIELDS = {"id", "route", "blocker", "question"}
ROUTES = {"ACT", "ASK"}
BLOCKERS = {"none", "behavior", "interface", "permission", "side_effect", "target"}


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def grade(answers: Any, key: Any) -> dict[str, Any]:
    expected = {item["id"]: item for item in key}
    expected_order = [item["id"] for item in key]
    seen: set[str] = set()
    route_correct = 0
    contract_correct = 0
    format_violations = 0
    details: list[dict[str, Any]] = []

    if not isinstance(answers, list):
        return {
            "total": len(expected),
            "route_correct": 0,
            "contract_correct": 0,
            "format_violations": len(expected),
            "details": [{"error": "top-level answer must be a JSON array"}],
        }

    for index, raw in enumerate(answers):
        errors: list[str] = []
        if not isinstance(raw, dict):
            format_violations += 1
            details.append({"error": "answer item is not an object"})
            continue

        case_id = raw.get("id")
        if set(raw) != FIELDS:
            errors.append("fields")
        if index >= len(expected_order) or case_id != expected_order[index]:
            errors.append("order")
        if case_id not in expected or case_id in seen:
            errors.append("id")
        if raw.get("route") not in ROUTES:
            errors.append("route_value")
        if raw.get("blocker") not in BLOCKERS:
            errors.append("blocker_value")

        route = raw.get("route")
        blocker = raw.get("blocker")
        question = raw.get("question")
        if route == "ACT" and (blocker != "none" or question is not None):
            errors.append("act_shape")
        if route == "ASK" and (
            blocker == "none"
            or not isinstance(question, str)
            or not question.strip()
        ):
            errors.append("ask_shape")

        if errors:
            format_violations += 1

        if case_id in expected and case_id not in seen:
            seen.add(case_id)
            target = expected[case_id]
            route_ok = route == target["route"]
            contract_ok = route_ok and blocker == target["blocker"]
            route_correct += int(route_ok)
            contract_correct += int(contract_ok)
            details.append(
                {
                    "id": case_id,
                    "route_ok": route_ok,
                    "contract_ok": contract_ok,
                    "format_errors": errors,
                }
            )
        else:
            details.append({"id": case_id, "format_errors": errors})

    missing = sorted(set(expected) - seen)
    format_violations += len(missing)
    details.extend({"id": case_id, "error": "missing"} for case_id in missing)

    return {
        "total": len(expected),
        "route_correct": route_correct,
        "contract_correct": contract_correct,
        "format_violations": format_violations,
        "details": details,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("answers", type=Path)
    parser.add_argument("key", type=Path)
    parser.add_argument("--details", action="store_true")
    args = parser.parse_args()

    result = grade(load_json(args.answers), load_json(args.key))
    if not args.details:
        result.pop("details", None)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
