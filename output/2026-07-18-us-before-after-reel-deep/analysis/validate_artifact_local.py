#!/usr/bin/env python3
"""Preflight the local artifact shape before the single MCP validation call."""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path


ARTIFACT = Path(__file__).parents[1] / "artifact.json"
PLUGIN_SCRIPTS = Path(
    "/Users/mehmetcan/.codex/plugins/cache/openai-curated-remote/"
    "data-analytics/0.2.8-13ceeea1f599/src/analytics-app/scripts"
)
sys.path.insert(0, str(PLUGIN_SCRIPTS))

from chart_contract import (  # noqa: E402
    validate_chart_data_compatibility,
    validate_chart_intent_metadata,
    validate_chart_presentation_options,
    validate_chart_type,
)


def main() -> None:
    payload = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    assert payload["surface"] == "report"
    manifest = payload["manifest"]
    snapshot = payload["snapshot"]
    datasets = snapshot["datasets"]
    blocks = manifest["blocks"]
    assert blocks[0]["type"] == "markdown"
    assert blocks[0]["body"] == f"# {manifest['title']}"
    assert blocks[1]["body"].startswith("## Executive Summary")
    assert any(block["type"] == "chart" for block in blocks)
    assert snapshot["status"] == "partial" and len(snapshot["accessIssues"]) == 2

    source_ids = {source["id"] for source in manifest["sources"]}
    assert len(source_ids) == len(manifest["sources"])
    assert source_ids == {source["id"] for source in payload["sources"]}
    database = ARTIFACT.parent / "analysis/report_sources.sqlite"
    with sqlite3.connect(database) as connection:
        for source in manifest["sources"]:
            rows = connection.execute(source["query"]["sql"]).fetchall()
            assert rows, f"Source query returned no rows: {source['id']}"

    block_chart_ids = {b["chartId"] for b in blocks if b["type"] == "chart"}
    chart_ids = {chart["id"] for chart in manifest["charts"]}
    assert block_chart_ids <= chart_ids
    for index, chart in enumerate(manifest["charts"]):
        path = f"manifest.charts[{index}]"
        rows = datasets[chart["dataset"]]
        assert chart["sourceId"] in source_ids
        validate_chart_type(chart["type"], path)
        validate_chart_intent_metadata(chart, path, require=True)
        validate_chart_presentation_options(chart, path)
        validate_chart_data_compatibility(chart, rows, path)

    block_table_ids = {b["tableId"] for b in blocks if b["type"] == "table"}
    table_ids = {table["id"] for table in manifest["tables"]}
    assert block_table_ids <= table_ids
    for table in manifest["tables"]:
        rows = datasets[table["dataset"]]
        fields = {column["field"] for column in table["columns"]}
        assert table["defaultSort"]["field"] in fields
        assert table["sourceId"] in source_ids
        assert all(any(column in row for row in rows) for column in fields)

    block_card_ids = {
        card_id
        for block in blocks
        if block["type"] == "metric-strip"
        for card_id in block["cardIds"]
    }
    cards = {card["id"]: card for card in manifest["cards"]}
    assert block_card_ids <= cards.keys()
    for card in cards.values():
        rows = datasets[card["dataset"]]
        assert card["sourceId"] in source_ids
        assert all(any(metric["field"] in row for row in rows) for metric in card["metrics"])

    print(
        "PASS local artifact preflight:",
        len(blocks),
        "blocks,",
        len(manifest["charts"]),
        "charts,",
        len(manifest["tables"]),
        "tables",
    )


if __name__ == "__main__":
    main()
