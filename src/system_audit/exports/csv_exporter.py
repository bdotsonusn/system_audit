from __future__ import annotations

import csv
from pathlib import Path
from typing import Any, Dict, Iterable, Tuple

from .base import AuditExporter


def _rows_from_report(report: Dict[str, Any]) -> Iterable[Tuple[str, str]]:
    for k, v in report.items():
        yield str(k), str(v)


class CSVExporter(AuditExporter):
    name = "csv"

    def export(self, report: Dict[str, Any], out_dir: Path) -> Path:
        out_dir.mkdir(parents=True, exist_ok=True)
        p = out_dir / "audit_report.csv"
        with p.open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["key", "value"])
            w.writerows(_rows_from_report(report))
        return p
