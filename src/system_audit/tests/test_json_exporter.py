import json
from pathlib import Path

from system_audit.exports.json_exporter import JSONExporter


def test_json_exporter_creates_file_and_writes_json(tmp_path: Path):
    exporter = JSONExporter()
    report = {"system": "audit", "status": "ok"}
    out_dir = tmp_path / "exports"

    output_path = exporter.export(report, out_dir)

    assert output_path.exists(), "Expected JSON file to be created"
    data = json.loads(output_path.read_text())
    assert data == report, "JSON contents should match input report"
    assert output_path.name == "audit_report.json"
