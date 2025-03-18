from abc import ABC, abstractmethod

class BaseProvider(ABC):
    """Abstract base class for all LLM providers."""

    @abstractmethod
    def check_server_availability(self) -> bool:
        """Check if the LLM server is available."""
        pass

    @abstractmethod
    def load_model(self):
        """Load the model for the provider."""
        pass

    @abstractmethod
    def generate_response(self, prompt: str, **kwargs) -> str:
        """Generate a response from the model based on the given prompt."""
        pass