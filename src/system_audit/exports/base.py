from __future__ import annotations
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict

class AuditExporter(ABC):
    """Abstract interface for audit report writers."""

    @abstractmethod
    def export(self, report: Dict[str, Any], out_dir: Path) -> Path:
        """Write report to out_dir and return created file path."""
        raise NotImplementedError