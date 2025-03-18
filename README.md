# LLM Framework

This project provides a framework for interacting with Large Language Models (LLMs) through various providers. It allows users to send prompts to different LLMs and receive responses, making it easier to integrate LLM capabilities into applications.

## Features

- **Multiple Providers**: Supports different LLM providers, including Ollama and LLaMA.
- **Client Interface**: A unified client interface for sending prompts and receiving responses.
- **Markdown Support**: Utility functions for saving responses in markdown format.
- **Testing**: Comprehensive unit tests for all components to ensure reliability.

## Installation

To install the LLM Framework, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd llm_framework
pip install -r requirements.txt
```

## Usage

### Initializing the Client

```python
from llm_framework.client import LLMClient
from llm_framework.providers.ollama_provider import OllamaProvider

provider = OllamaProvider(model_name="llama2")
client = LLMClient(provider)
```

### Sending a Prompt

```python
response = client.prompt("Explain what a transformer model is in simple terms.")
print(response.text)
```

### Saving Responses

```python
client.save_response_to_markdown(response, "response.md", "Transformer Explanation")
```

## Running Tests

To run the tests, use the following command:

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.