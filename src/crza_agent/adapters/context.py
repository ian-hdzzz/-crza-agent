"""Adapters — context engineering (Slot 4).

PassthroughContext: passes history as-is.
FirmContextPolicy: injects the CRZ//A knowledge block into the instructions.
"""
from __future__ import annotations

from typing import Sequence

from ..application.ports import ContextPolicy, Message, ModelRequest


class PassthroughContext:
    """Passes instructions and history unchanged to the model."""

    def build(self, instructions: str, history: Sequence[Message]) -> ModelRequest:
        return ModelRequest(
            instructions=instructions,
            messages=tuple(history),
        )


class FirmContextPolicy:
    """Prepends the firm's knowledge block to every model call.

    Slot 4 choice: static context injection (Placement A from doc 05) —
    the knowledge is small enough to fit in every call's context window.
    No RAG database needed.
    """

    def __init__(self, knowledge_block: str) -> None:
        self._knowledge = knowledge_block

    def build(self, instructions: str, history: Sequence[Message]) -> ModelRequest:
        enriched_instructions = instructions + "\n\n" + self._knowledge
        return ModelRequest(
            instructions=enriched_instructions,
            messages=tuple(history),
        )
