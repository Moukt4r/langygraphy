"""LLM client interface and implementations."""

from abc import ABC, abstractmethod


class LLMClient(ABC):
    """Abstract base class for LLM clients."""

    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate text response from the LLM.

        Args:
            prompt: Input text prompt
            **kwargs: Additional generation parameters

        Returns:
            Generated text response
        """
        ...


class DummyLLM(LLMClient):
    """Placeholder implementation; replace with real provider (OpenAI, Ollama, etc.)."""

    def generate(self, prompt: str, **kwargs) -> str:
        """Raise NotImplementedError to indicate this is a placeholder."""
        raise NotImplementedError("Plug in a real LLM client here.")
