"""Infrastructure adapter — Anthropic Claude via the Anthropic SDK.

This is the ONLY place that imports the anthropic package.
Implements ModelPort: takes a ModelRequest, returns a Respond.
"""
from __future__ import annotations

import os

import anthropic

from ..application.ports import Message, ModelRequest, Respond


class AnthropicModelAdapter:
    """Wraps Claude behind ModelPort. Model choice is a composition-root
    decision, passed here as a constructor argument."""

    def __init__(self, model_id: str = "claude-haiku-4-5-20251001") -> None:
        self._model_id = model_id
        self._client = anthropic.Anthropic(
            api_key=os.environ["ANTHROPIC_API_KEY"]
        )

    def decide(self, request: ModelRequest) -> Respond:
        messages = self._to_anthropic_messages(request.messages)

        response = self._client.messages.create(
            model=self._model_id,
            max_tokens=1024,
            system=request.instructions,
            messages=messages,
        )

        text = response.content[0].text if response.content else ""
        return Respond(text=text)

    @staticmethod
    def _to_anthropic_messages(messages: tuple[Message, ...]) -> list[dict]:
        """Convert internal Message types to Anthropic's wire format.
        Roles must strictly alternate user/assistant for Anthropic."""
        result: list[dict] = []
        for msg in messages:
            role = "user" if msg.role == "user" else "assistant"
            # Merge consecutive same-role messages (Anthropic requirement)
            if result and result[-1]["role"] == role:
                result[-1]["content"] += "\n" + msg.content
            else:
                result.append({"role": role, "content": msg.content})
        return result
