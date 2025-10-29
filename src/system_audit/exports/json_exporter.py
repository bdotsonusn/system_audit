import json
from pathlib import Path
from typing import Any, Dict
from .base import AuditExporter

class JSONExporter(AuditExporter):
    name = "json"

    def export(self, report: Dict[str, Any], out_dir: Path) -> Path:
        out_dir.mkdir(parents=True, exist_ok=True)
        p = out_dir / "audit_report.json"
        p.write_text(json.dumps(report, indent=2))
        return p