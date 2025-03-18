import unittest
from llm_framework.providers.llama_provider import LlamaProvider
from llm_framework.client import LLMClient

class TestLlamaProvider(unittest.TestCase):

    def setUp(self):
        model_path = "/path/to/your/model.gguf"  # Update with the actual model path
        self.provider = LlamaProvider(model_path=model_path)
        self.client = LLMClient(self.provider)

    def test_server_availability(self):
        self.assertTrue(self.provider.check_server_availability(), "LLaMA server should be available.")

    def test_prompt_response(self):
        prompt = "What is the capital of France?"
        response = self.client.prompt(prompt)
        self.assertIsNotNone(response.text, "Response text should not be None.")
        self.assertIn("Paris", response.text, "Response should mention Paris.")

    def test_chat_response(self):
        messages = [
            {"role": "user", "content": "Tell me about Python."},
            {"role": "assistant", "content": "Python is a programming language."}
        ]
        response = self.client.chat(messages)
        self.assertIsNotNone(response.text, "Response text should not be None.")
        self.assertEqual(response.text, "This is a mock chat response.")

if __name__ == "__main__":
    unittest.main()