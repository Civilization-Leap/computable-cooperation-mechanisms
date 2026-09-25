"""Read-only JSON stdin/stdout comparison export for Purpose Generation."""

from __future__ import annotations

import json
import sys
from typing import Any

from mechanism_ref.comparison import (
    AssumptionVariant,
    ChannelState,
    Plan,
    UnknownRange,
    assumption_reversal,
    channel_boundary_flags,
    compare_plans,
    unknown_dependency,
)


def export_comparison(payload: dict[str, Any]) -> dict[str, Any]:
    plans = tuple(
        Plan(str(item["plan_id"]), {str(k): float(v) for k, v in item["components"].items()})
        for item in payload["plans"]
    )
    base = compare_plans(plans)

    unknowns = []
    for item in payload.get("unknown_ranges", ()):
        dep = unknown_dependency(
            plans,
            plan_id=str(item["plan_id"]),
            unknown=UnknownRange(str(item["component"]), float(item["low"]), float(item["high"])),
        )
        if dep is not None:
            unknowns.append({"unknown_id": dep["unknown_id"], "effect": dep["effect"]})

    variants = tuple(
        AssumptionVariant(
            str(item["variant_id"]),
            str(item["plan_id"]),
            str(item["component"]),
            float(item["value"]),
        )
        for item in payload.get("assumption_variants", ())
    )
    reversal = assumption_reversal(plans, variants) if variants else None
    reversals = []
    if reversal is not None:
        reversals = [str(item["variant_id"]) for item in reversal["changed_variants"]]

    boundary_flags = []
    if "baseline_channels" in payload or "candidate_channels" in payload:
        before = tuple(ChannelState(**item) for item in payload.get("baseline_channels", ()))
        after = tuple(ChannelState(**item) for item in payload.get("candidate_channels", ()))
        boundary_flags = channel_boundary_flags(before, after)

    return {
        "schema_version": "0.1",
        "non_dominated": base["non_dominated"],
        "dominated": base["dominated"],
        "incomparable": base["incomparable"],
        "unknown_dependent": unknowns,
        "assumption_reversals": reversals,
        "boundary_flags": boundary_flags,
    }


def main() -> int:
    payload = json.load(sys.stdin)
    if not isinstance(payload, dict):
        raise SystemExit("input must be a JSON object")
    json.dump(export_comparison(payload), sys.stdout, ensure_ascii=False, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
