"""Trace adapters. PrintTrace for local dev, NullTrace for tests."""
from __future__ import annotations

import json


class PrintTrace:
    def event(self, kind: str, payload: dict) -> None:
        print(f"[TRACE] {kind}: {json.dumps(payload, ensure_ascii=False)}")


class NullTrace:
    def event(self, kind: str, payload: dict) -> None:
        pass
