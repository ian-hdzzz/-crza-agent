"""Infrastructure layer — FastAPI HTTP server.

Exposes POST /chat. CORS is open for local development;
restrict origins in production via ALLOWED_ORIGINS env var.
"""
from __future__ import annotations

import os
from typing import Sequence

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ..application.agents import AgentSpec
from ..application.ports import ContextPolicy, Message, ModelPort, TracePort


# ---------------------------------------------------------------------------
# Request / response schemas
# ---------------------------------------------------------------------------

class HistoryMessage(BaseModel):
    role: str     # "user" | "assistant"
    content: str


class ChatRequest(BaseModel):
    message: str
    history: list[HistoryMessage] = []


class ChatResponse(BaseModel):
    response: str


# ---------------------------------------------------------------------------
# App factory
# ---------------------------------------------------------------------------

def create_app(
    spec: AgentSpec,
    model: ModelPort,
    context: ContextPolicy,
    trace: TracePort,
) -> FastAPI:
    app = FastAPI(
        title="CRZ//A Legal Assistant",
        description="Agente de inteligencia legal para CRZ//A Abogados.",
        version="1.0.0",
    )

    allowed_origins = os.environ.get("ALLOWED_ORIGINS", "*").split(",")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["POST", "GET", "OPTIONS"],
        allow_headers=["*"],
    )

    @app.get("/health")
    async def health() -> dict:
        return {"status": "ok", "agent": spec.name}

    @app.post("/chat", response_model=ChatResponse)
    async def chat(body: ChatRequest) -> ChatResponse:
        # Convert wire messages → internal Message types
        history: list[Message] = [
            Message(
                role=m.role,
                content=m.content,
                origin="principal" if m.role == "user" else "internal",
            )
            for m in body.history
        ]

        # Append the new user message
        history.append(Message(role="user", content=body.message, origin="principal"))

        # Slot 4: build the transient model request
        request = context.build(
            instructions=spec.instructions,
            history=history,
        )

        trace.event("request", {"agent": spec.name, "message": body.message})

        # Slot 3: single model call (no tools, no delegation)
        action = model.decide(request)

        trace.event("response", {"agent": spec.name, "chars": len(action.text)})

        return ChatResponse(response=action.text)

    return app
