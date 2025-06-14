"""LangGraph integration and graph building utilities."""

from typing import Any

from langgraph.graph import StateGraph

from .llm import DummyLLM, LLMClient


def build_simple_graph(llm: LLMClient | None = None) -> StateGraph:
    """Build a simple graph with one LLM node.

    Args:
        llm: LLM client to use. Defaults to DummyLLM if not provided.

    Returns:
        Configured StateGraph instance
    """
    llm = llm or DummyLLM()
    graph = StateGraph(dict[str, Any])

    def llm_node(state: dict[str, Any]) -> dict[str, Any]:
        """Node that calls the LLM with the prompt from state."""
        # Delegate to the placeholder LLM
        response = llm.generate(prompt=state["prompt"])
        return {"response": response}

    graph.add_node("llm", llm_node)
    graph.add_edge("__start__", "llm")
    graph.add_edge("llm", "__end__")

    return graph


if __name__ == "__main__":
    # Demo: build a graph without importing heavy LLM deps
    graph = build_simple_graph()
    print("Graph built successfully with nodes:", list(graph.nodes.keys()))
