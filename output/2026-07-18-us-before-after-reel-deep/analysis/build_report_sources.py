#!/usr/bin/env python3
"""Materialize reviewed artifact datasets into a local SQLite source database."""

from __future__ import annotations

import json
import re
import sqlite3
from pathlib import Path


ROOT = Path(__file__).parents[1]
ARTIFACT = ROOT / "artifact.json"
DATABASE = ROOT / "analysis/report_sources.sqlite"
IDENTIFIER = re.compile(r"^[a-z][a-z0-9_]*$")


def sqlite_type(values: list[object]) -> str:
    non_null = [value for value in values if value is not None]
    if non_null and all(isinstance(value, bool | int) and not isinstance(value, float) for value in non_null):
        return "INTEGER"
    if non_null and all(isinstance(value, int | float) and not isinstance(value, bool) for value in non_null):
        return "REAL"
    return "TEXT"


def normalize(value: object) -> object:
    if value is None or isinstance(value, str | int | float):
        return value
    if isinstance(value, bool):
        return int(value)
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def main() -> None:
    payload = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    datasets = payload["snapshot"]["datasets"]
    if DATABASE.exists():
        DATABASE.unlink()
    connection = sqlite3.connect(DATABASE)
    try:
        for table, rows in datasets.items():
            if not IDENTIFIER.fullmatch(table):
                raise ValueError(f"Unsafe table identifier: {table}")
            if not rows:
                continue
            columns = list(rows[0])
            if any(not IDENTIFIER.fullmatch(column) for column in columns):
                raise ValueError(f"Unsafe column identifier in {table}")
            declarations = [
                f'"{column}" {sqlite_type([row.get(column) for row in rows])}'
                for column in columns
            ]
            connection.execute(f'CREATE TABLE "{table}" ({", ".join(declarations)})')
            placeholders = ", ".join("?" for _ in columns)
            quoted = ", ".join(f'"{column}"' for column in columns)
            connection.executemany(
                f'INSERT INTO "{table}" ({quoted}) VALUES ({placeholders})',
                [[normalize(row.get(column)) for column in columns] for row in rows],
            )
        connection.commit()
        table_count = connection.execute(
            "SELECT COUNT(*) FROM sqlite_master WHERE type = 'table'"
        ).fetchone()[0]
        print(f"WROTE {DATABASE} with {table_count} tables")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
