from llm_framework.client import LLMClient
from llm_framework.providers.base_provider import BaseProvider
import unittest
from unittest.mock import MagicMock
from datetime import datetime  # Import datetime module

class TestLLMClient(unittest.TestCase):

    def setUp(self):
        self.provider = MagicMock(spec=BaseProvider)
        self.client = LLMClient(self.provider)

    def test_prompt(self):
        prompt_text = "What is AI?"
        expected_response = "AI stands for Artificial Intelligence."
        self.provider.generate_response.return_value.text = expected_response
        
        response = self.client.prompt(prompt_text)
        
        self.provider.generate_response.assert_called_once_with(prompt_text,0.7)
        self.assertEqual(response.text, expected_response)

    def test_save_response_to_markdown(self):
        response = MagicMock()
        response.text = "Sample response text."
        response.model = "test_model"
        response.usage = {
            "prompt_tokens": 10,
            "completion_tokens": 5,
            "total_tokens": 15
        }
        
        file_path = "test_response.md"
        self.client.save_response_to_markdown(response, file_path, "Test Title")
        
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Update the expected content to match the actual content format
        expected_content = (
            "# Test Title\n\n"
            "**Model:** test_model\n"
            "**Token usage:** {'prompt_tokens': 10, 'completion_tokens': 5, 'total_tokens': 15}\n\n"
            "## Response\n\n"
            "Sample response text.\n\n"
            "---\n"
            f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
        )
        self.assertEqual(content.strip(), expected_content.strip())

if __name__ == "__main__":
    unittest.main()