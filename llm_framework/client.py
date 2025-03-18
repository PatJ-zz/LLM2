from llm_framework.providers.base_provider import BaseProvider
from llm_framework.utils.markdown_utils import save_response_to_markdown

class LLMClient:
    def __init__(self, provider: BaseProvider):
        self.provider = provider

    def prompt(self, prompt: str, temperature: float = 0.7):
        response = self.provider.generate_response(prompt, temperature)
        return response

    def chat(self, messages: list, temperature: float = 0.7):
        response = self.provider.generate_chat_response(messages, temperature)
        return response

    def save_response_to_markdown(self, response, file_path: str, title: str):
        save_response_to_markdown(response, file_path, title)