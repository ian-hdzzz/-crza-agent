"""Tier-1 evals (Slot 6) — scripted, no real model calls.

Run: python -m pytest tests/ -v
"""
from __future__ import annotations

import pytest

from src.crza_agent.adapters.context import FirmContextPolicy
from src.crza_agent.adapters.trace import NullTrace
from src.crza_agent.application.agents import AgentSpec, GuardRails
from src.crza_agent.application.ports import Message, Respond
from src.crza_agent.domain.knowledge import (
    CONTACT,
    CREDENTIALS,
    DESKS,
    FIRM_NAME,
    PRACTICE_AREAS,
    build_knowledge_block,
)


# ---------------------------------------------------------------------------
# Domain layer tests — pure, deterministic
# ---------------------------------------------------------------------------

def test_knowledge_block_contains_firm_name():
    block = build_knowledge_block()
    assert FIRM_NAME in block


def test_knowledge_block_contains_all_desks():
    block = build_knowledge_block()
    for desk in DESKS:
        assert desk in block


def test_knowledge_block_contains_contact():
    block = build_knowledge_block()
    assert CONTACT["email_general"] in block
    assert CONTACT["phone_bernardo"] in block


def test_knowledge_block_contains_credentials():
    block = build_knowledge_block()
    assert "WFZO" in block
    assert "Tops México" in block


# ---------------------------------------------------------------------------
# Context policy tests
# ---------------------------------------------------------------------------

def test_firm_context_policy_enriches_instructions():
    policy = FirmContextPolicy(knowledge_block="KNOWLEDGE_HERE")
    request = policy.build(instructions="Base instructions.", history=[])
    assert "Base instructions." in request.instructions
    assert "KNOWLEDGE_HERE" in request.instructions


def test_firm_context_policy_passes_history():
    policy = FirmContextPolicy(knowledge_block="K")
    history = [
        Message(role="user", content="Hola"),
        Message(role="assistant", content="Hola, ¿en qué te puedo ayudar?"),
    ]
    request = policy.build(instructions="I", history=history)
    assert len(request.messages) == 2
    assert request.messages[0].content == "Hola"


# ---------------------------------------------------------------------------
# AgentSpec tests
# ---------------------------------------------------------------------------

def test_agent_spec_guardrails_defaults():
    spec = AgentSpec(name="test", description="desc", instructions="inst")
    assert spec.guardrails.max_steps == 3
    assert spec.guardrails.max_consecutive_errors == 2


# ---------------------------------------------------------------------------
# Fake model for integration path test
# ---------------------------------------------------------------------------

class FakeModel:
    """Returns a scripted Respond. The ONLY non-determinism in the system
    is behind ModelPort — so stubbing it makes the whole path deterministic."""
    def __init__(self, reply: str) -> None:
        self._reply = reply

    def decide(self, request) -> Respond:
        return Respond(text=self._reply)


def test_server_happy_path():
    """Integration: request reaches the model and response comes back."""
    from fastapi.testclient import TestClient
    from src.crza_agent.infrastructure.server import create_app

    spec = AgentSpec(name="test", description="d", instructions="i")
    app = create_app(
        spec=spec,
        model=FakeModel("Hola desde CRZ//A."),
        context=FirmContextPolicy(knowledge_block="K"),
        trace=NullTrace(),
    )
    client = TestClient(app)
    response = client.post("/chat", json={"message": "¿Qué hacen?"})
    assert response.status_code == 200
    assert response.json()["response"] == "Hola desde CRZ//A."


def test_server_health():
    from fastapi.testclient import TestClient
    from src.crza_agent.infrastructure.server import create_app

    spec = AgentSpec(name="test", description="d", instructions="i")
    app = create_app(
        spec=spec,
        model=FakeModel("ok"),
        context=FirmContextPolicy(knowledge_block="K"),
        trace=NullTrace(),
    )
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
