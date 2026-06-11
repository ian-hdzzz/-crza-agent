"""Gemini adapter — implementa ModelPort usando google-genai SDK."""
from __future__ import annotations

import os
from google import genai
from google.genai import types

from ..application.ports import ModelRequest, Respond


class GeminiModelAdapter:
    def __init__(self, model_id: str = "gemini-2.0-flash") -> None:
        self._model_id = model_id
        self._client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    def decide(self, request: ModelRequest) -> Respond:
        # Convierte historial interno → formato Gemini
        contents = [
            types.Content(
                role="user" if m.role == "user" else "model",
                parts=[types.Part(text=m.content)],
            )
            for m in request.messages
        ]

        response = self._client.models.generate_content(
            model=self._model_id,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=request.instructions,
                max_output_tokens=1024,
                temperature=0.7,
            ),
        )

        return Respond(text=response.text or "")
