"""Application ports — interfaces the core depends on.

Simplified subset of the full template ports.py, scoped to what a
single-agent conversational chatbot actually needs.

Dependency rule: only stdlib imports here.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal, Protocol, Sequence


Origin = Literal["operator", "principal", "internal", "external"]


@dataclass(frozen=True)
class Message:
    role: str          # "user" | "assistant"
    content: str
    origin: Origin = "principal"


@dataclass(frozen=True)
class ModelRequest:
    """Transient view — built fresh on every call by the ContextPolicy."""
    instructions: str
    messages: tuple[Message, ...]


@dataclass(frozen=True)
class Respond:
    text: str


class ModelPort(Protocol):
    """One cognitive turn. The only place nondeterminism enters the core."""
    def decide(self, request: ModelRequest) -> Respond: ...


class ContextPolicy(Protocol):
    """Takes raw history → builds the transient ModelRequest for one call."""
    def build(self, instructions: str, history: Sequence[Message]) -> ModelRequest: ...


class TracePort(Protocol):
    def event(self, kind: str, payload: dict) -> None: ...
