from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict

class AuditExporter(ABC):
    name: str = "base"

    @abstractmethod
    def export(self, report: Dict[str, Any], out_dir: Path) -> Path:
        ...