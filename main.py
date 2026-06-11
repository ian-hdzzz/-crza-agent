"""Composition root — the only file that knows about everything.

Wires domain knowledge + AgentSpec + adapters + topology.
Run locally:  uvicorn main:app --reload --port 8000
"""
from __future__ import annotations

from src.crza_agent.adapters.anthropic_model import AnthropicModelAdapter
from src.crza_agent.adapters.context import FirmContextPolicy
from src.crza_agent.adapters.trace import PrintTrace
from src.crza_agent.application.agents import AgentSpec, GuardRails
from src.crza_agent.domain.knowledge import build_knowledge_block
from src.crza_agent.infrastructure.server import create_app

# ---------------------------------------------------------------------------
# Slot 1 — Domain knowledge loaded once at startup
# ---------------------------------------------------------------------------

KNOWLEDGE_BLOCK = build_knowledge_block()

# ---------------------------------------------------------------------------
# Slot 3 — Single agent spec (no delegation needed for a chat assistant)
# Slot 5 — Guardrails: max_steps=3, conservative for a public-facing bot
# ---------------------------------------------------------------------------

CRZA_AGENT = AgentSpec(
    name="crza_assistant",
    description="Asistente de inteligencia legal de CRZ//A Abogados.",
    instructions=(
        "Eres el asistente virtual de CRZ//A Abogados (Cuenca Reyes Zavala y Asociados), "
        "una firma líder de estrategia, inteligencia comercial y servicios jurídicos "
        "internacionales con 12 años de trayectoria.\n\n"
        "Tu rol es responder preguntas sobre la firma: sus servicios, equipo, presencia "
        "internacional, credenciales y cómo contactarlos. Responde siempre en español "
        "de manera profesional, concisa y cálida. Si la pregunta está fuera del alcance "
        "de la firma, invita amablemente al usuario a contactar directamente al equipo "
        "a través de contacto@crza.com.mx o al teléfono 55 2139 5193.\n\n"
        "NO inventes información. Si no tienes el dato en el bloque de conocimiento, "
        "di que no tienes esa información y sugiere contactar a la firma."
    ),
    guardrails=GuardRails(max_steps=3, max_consecutive_errors=2),
)

# ---------------------------------------------------------------------------
# Wiring (Slot 4: FirmContextPolicy injects the knowledge block)
# ---------------------------------------------------------------------------

app = create_app(
    spec=CRZA_AGENT,
    model=AnthropicModelAdapter(model_id="claude-haiku-4-5-20251001"),
    context=FirmContextPolicy(knowledge_block=KNOWLEDGE_BLOCK),
    trace=PrintTrace(),
)
