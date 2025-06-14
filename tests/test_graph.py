"""Tests for the graph module."""

import pytest

from tools.graph import build_simple_graph


def test_dummy_llm_not_implemented():
    """Test that the graph builds and DummyLLM raises NotImplementedError."""
    g = build_simple_graph()
    exec = g.compile()

    with pytest.raises(NotImplementedError, match="Plug in a real LLM client here"):
        exec.invoke({"prompt": "hello"})
