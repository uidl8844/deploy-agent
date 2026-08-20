from __future__ import annotations
from dataclasses import dataclass, asdict
import hashlib
from pathlib import Path

@dataclass
class Release:
    version: str
    sha256: str
    artifact: str = ""

class ReleaseLog:
    def __init__(self):
        self._items: list[Release] = []
    def record(self, version: str, sha256: str, artifact: str = "") -> Release:
        if not version.strip():
            raise ValueError("version required")
        if len(sha256) < 8:
            raise ValueError("sha256 too short")
        rel = Release(version.strip(), sha256.lower(), artifact)
        self._items.append(rel)
        return rel
    def current(self) -> Release | None:
        return self._items[-1] if self._items else None
    def rollback_target(self) -> Release | None:
        return self._items[-2] if len(self._items) >= 2 else None
    def history(self) -> list[Release]:
        return list(self._items)

def file_sha256(path: str | Path) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()
