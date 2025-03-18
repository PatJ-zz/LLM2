import unittest
from llm_framework.providers.ollama_provider import OllamaProvider
from llm_framework.client import LLMClient
import os

class TestOllamaProvider(unittest.TestCase):

    def setUp(self):
        self.model_name = "llama2"  # Replace with a valid model name
        self.provider = OllamaProvider(model_name=self.model_name)
        self.client = LLMClient(self.provider)

    def test_server_availability(self):
        self.assertTrue(self.provider.check_server_availability(), "Ollama server should be available.")

    def test_prompt_response(self):
        prompt = "What is artificial intelligence?"
        response = self.client.prompt(prompt, temperature=0.7)
        self.assertIsNotNone(response.text, "Response text should not be None.")
        self.assertGreater(len(response.text), 0, "Response text should not be empty.")

    def test_save_response_to_markdown(self):
        prompt = "Explain the concept of neural networks."
        response = self.client.prompt(prompt, temperature=0.7)
        markdown_file = "neural_networks_explanation.md"
        self.client.save_response_to_markdown(response, markdown_file, "Neural Networks Explained")
        
        # Check if the markdown file was created
        self.assertTrue(os.path.exists(markdown_file), "Markdown file should be created.")

if __name__ == "__main__":
    unittest.main()