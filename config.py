"""
Configuration file for Student AI Travel Planner
This file manages API provider configuration and loads keys from environment variables.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env if it exists in the project root
PROJECT_ROOT = Path(__file__).resolve().parent
ENV_PATH = PROJECT_ROOT / ".env"
if ENV_PATH.exists():
    load_dotenv(dotenv_path=ENV_PATH)

AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini").strip().lower()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b").strip()

def get_provider():
    """
    Returns the configured AI provider.

    Returns:
        str: Current provider name (gemini, openai, or groq)
    """
    return AI_PROVIDER

def get_api_key():
    """
    Returns the API key for the selected provider.

    Returns:
        str: API key for the configured provider

    Raises:
        ValueError: If no API key is set for the provider
    """
    if AI_PROVIDER == "gemini":
        if not GEMINI_API_KEY:
            raise ValueError(
                "Gemini API key not set. Please add GEMINI_API_KEY to .env or your environment variables."
            )
        return GEMINI_API_KEY
    elif AI_PROVIDER == "openai":
        if not OPENAI_API_KEY:
            raise ValueError(
                "OpenAI API key not set. Please add OPENAI_API_KEY to .env or your environment variables."
            )
        return OPENAI_API_KEY
    elif AI_PROVIDER == "groq":
        if not GROQ_API_KEY:
            raise ValueError(
                "Groq API key not set. Please add GROQ_API_KEY to .env or your environment variables."
            )
        return GROQ_API_KEY
    else:
        raise ValueError(
            f"Unknown AI provider '{AI_PROVIDER}'. Set AI_PROVIDER to 'gemini', 'openai', or 'groq'."
        )

def get_groq_model():
    """
    Returns the configured Groq model name.

    Returns:
        str: Groq model identifier
    """
    return GROQ_MODEL
