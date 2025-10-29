from pathlib import Path
import os

from system_audit.exports.csv_exporter import CSVExporter


def test_csv_exporter_writes_file(tmp_path: Path):
    # Arrange
    report = {"alpha": 1, "beta": 2}
    out_dir = tmp_path / "out"

    # Act
    p = CSVExporter().export(report=report, out_dir=out_dir)

    # Assert
    assert isinstance(p, Path)
    assert p.suffix.lower() == ".csv"
    assert p.exists()
    # File should be non-empty
    assert p.stat().st_size > 0