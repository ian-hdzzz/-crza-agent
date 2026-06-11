"""Agents as data — Slot 3 (single agent) + Slot 5 (guardrails).

AgentSpec is a declarative description: no behavior, no framework types.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class GuardRails:
    max_steps: int = 3               # For a chat agent, 1 is enough; 3 for safety.
    max_consecutive_errors: int = 2


@dataclass(frozen=True)
class AgentSpec:
    name: str
    description: str
    instructions: str                # The prompt — versioned artifact, owned here.
    guardrails: GuardRails = field(default_factory=GuardRails)
