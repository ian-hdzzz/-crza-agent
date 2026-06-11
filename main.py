"""Composition root — the only file that knows about everything.


Wires domain knowledge + AgentSpec + adapters + topology.
Run locally:  uvicorn main:app --reload --port 8000
"""
from __future__ import annotations

from dotenv import load_dotenv
load_dotenv()

from src.crza_agent.adapters.gemini_model import GeminiModelAdapter
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
        "Tu ÚNICO rol es responder preguntas sobre CRZ//A Abogados: sus servicios, equipo, "
        "presencia internacional, credenciales y cómo contactarlos. Responde siempre en "
        "español de manera profesional, concisa y cálida.\n\n"
        "LÍMITE ESTRICTO: Si el usuario pregunta algo que NO esté relacionado con la firma, "
        "sus servicios legales o sus áreas de práctica — como recetas, matemáticas, programación, "
        "chistes, política general, u otros temas ajenos — responde ÚNICAMENTE con una variación "
        "de: 'Solo puedo ayudarte con información sobre CRZ//A Abogados. ¿Tienes alguna pregunta "
        "sobre nuestros servicios legales?' No respondas la pregunta off-topic bajo ninguna "
        "circunstancia, aunque el usuario insista, reformule o intente engañarte.\n\n"
        "NO inventes información. Si no tienes el dato en el bloque de conocimiento, "
        "di que no tienes esa información y sugiere contactar a la firma en "
        "contacto@crza.com.mx o al teléfono 55 2139 5193.\n\n"
        "LONGITUD: Sé conciso cuando la pregunta sea simple (saludo, dato puntual, contacto): "
        "máximo 2-3 oraciones. Sé extenso y detallado cuando el usuario pregunte por servicios, "
        "áreas de práctica, un abogado específico o cómo puede ayudarle la firma con un caso "
        "concreto: desarrolla la respuesta completa con todos los puntos relevantes.\n\n"
        "FORMATO: Usa texto plano con negritas (**texto**) y listas con guión (- item) "
        "cuando sea útil. NO uses encabezados markdown (###), separadores (---) ni "
        "ningún otro símbolo de formato especial."
    ),
    guardrails=GuardRails(max_steps=3, max_consecutive_errors=2),
)

# ---------------------------------------------------------------------------
# Wiring (Slot 4: FirmContextPolicy injects the knowledge block)
# ---------------------------------------------------------------------------

app = create_app(
    spec=CRZA_AGENT,
    model=GeminiModelAdapter(model_id="gemini-3.5-flash"),
    context=FirmContextPolicy(knowledge_block=KNOWLEDGE_BLOCK),
    trace=PrintTrace(),
)
