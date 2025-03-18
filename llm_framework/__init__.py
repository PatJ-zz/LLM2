# FILE: /llm_framework/llm_framework/llm_framework/__init__.py

"""
llm_framework package

This package provides an interface for interacting with various Large Language Models (LLMs).
It includes client classes for sending prompts and receiving responses, as well as provider
classes for specific LLM implementations.
"""

from .client import LLMClient
from .providers import OllamaProvider, LlamaProvider
from .utils import markdown_utils