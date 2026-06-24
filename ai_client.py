"""
AI Client wrapper for Student AI Travel Planner
This module handles communication with Gemini and OpenAI APIs.
"""

import json
from config import get_api_key, get_provider, get_groq_model

# Import Gemini library (with error handling for missing package)
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

# Import OpenAI library (with error handling for missing package)
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


def generate_itinerary(prompt: str) -> str:
    """
    Generate travel itinerary using the configured AI provider.
    
    Args:
        prompt (str): The prompt containing travel details and requirements
        
    Returns:
        str: Raw AI response containing the itinerary
        
    Raises:
        Exception: If API call fails or provider is not available
    """
    api_key = get_api_key()
    provider = get_provider()

    if provider == "gemini":
        if not GEMINI_AVAILABLE:
            raise Exception("Gemini requires 'google-generativeai' package. Install with: pip install google-generativeai")
        return _call_gemini(prompt, api_key)
    elif provider == "openai":
        if not OPENAI_AVAILABLE:
            raise Exception("OpenAI requires 'openai' package. Install with: pip install openai")
        return _call_openai(prompt, api_key)
    elif provider == "groq":
        if not OPENAI_AVAILABLE:
            raise Exception("Groq provider requires 'openai'. Install with: pip install openai")
        return _call_groq(prompt, api_key)
    else:
        raise ValueError(f"Unknown AI provider '{provider}'. Set AI_PROVIDER to 'gemini', 'openai', or 'groq'.")


def _call_gemini(prompt: str, api_key: str) -> str:
    """
    Call Google Gemini API.
    
    Args:
        prompt (str): The prompt to send
        api_key (str): Gemini API key
        
    Returns:
        str: Gemini response
    """
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    return response.text


def _call_openai(prompt: str, api_key: str) -> str:
    """
    Call OpenAI API.
    
    Args:
        prompt (str): The prompt to send
        api_key (str): OpenAI API key
        
    Returns:
        str: OpenAI response
    """
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are an expert travel planner specializing in budget-friendly student trips."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=900
    )
    # The new OpenAI client returns structured messages; extract text safely.
    if hasattr(response.choices[0].message, 'content'):
        return response.choices[0].message.content.strip()
    if isinstance(response.choices[0].message, dict):
        content = response.choices[0].message.get('content')
        if isinstance(content, list) and len(content) > 0:
            return content[0].get('text', '').strip()
    return str(response)


def _call_groq(prompt: str, api_key: str) -> str:
    """
    Call Groq via the OpenAI-compatible Groq API endpoint.
    
    Args:
        prompt (str): The prompt to send
        api_key (str): Groq API key
        
    Returns:
        str: Groq response
    """
    model = get_groq_model()
    if not model.startswith("openai/"):
        raise ValueError(
            "Groq models must use OpenAI-compatible naming, e.g. 'openai/gpt-oss-20b'. "
            f"Got: '{model}'"
        )

    client = openai.OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")
    response = client.responses.create(
        model=model,
        input=prompt,
        temperature=0.7,
        max_output_tokens=900
    )
    if hasattr(response, "output_text") and response.output_text:
        return response.output_text.strip()
    if hasattr(response, "output") and response.output:
        return str(response.output).strip()
    return str(response)


def _parse_groq_output(data):
    if not data:
        return ""

    output = data.get("output") or data.get("outputs")
    if output is None:
        return str(data)

    if isinstance(output, list) and len(output) > 0:
        first = output[0]
        if isinstance(first, list) and len(first) > 0:
            first = first[0]
        if isinstance(first, dict):
            text = first.get("content") or first.get("text") or first.get("output")
            if isinstance(text, list) and len(text) > 0:
                return text[0].strip()
            if isinstance(text, str):
                return text.strip()
        if isinstance(first, str):
            return first.strip()
    return str(output)


def _get_dummy_response() -> str:
    """
    Returns a dummy response for testing when no API key is available.
    
    Returns:
        str: Sample JSON itinerary for testing
    """
    dummy_data = {
        "itinerary": [
            {
                "day": 1,
                "activities": [
                    "Visit the Eiffel Tower (student discount available)",
                    "Explore Montmartre district",
                    "Try street food at local markets"
                ],
                "cost": 45,
                "transport": "metro",
                "notes": "Student ID required for discounts. Free walking tour available."
            },
            {
                "day": 2,
                "activities": [
                    "Louvre Museum (free for EU students under 26)",
                    "Walk along the Seine River",
                    "Visit Notre-Dame Cathedral (exterior only)"
                ],
                "cost": 25,
                "transport": "metro + walking",
                "notes": "Book Louvre tickets online to skip queues."
            },
            {
                "day": 3,
                "activities": [
                    "Day trip to Versailles (half-day)",
                    "Explore Latin Quarter",
                    "Evening: Seine River cruise"
                ],
                "cost": 55,
                "transport": "train + metro",
                "notes": "Versailles has student discounts. Book river cruise in advance."
            }
        ],
        "summary": "A fantastic 3-day student adventure in Paris! This budget-friendly itinerary includes iconic landmarks, cultural experiences, and local cuisine. Total estimated cost: $125, well within your $200 budget. Highlights include free student discounts at major attractions, efficient metro transport, and authentic local experiences. Perfect for students who want to see the best of Paris without breaking the bank!"
    }
    
    return json.dumps(dummy_data, indent=2)


def test_provider_availability():
    """
    Test if the configured AI provider is available and properly configured.
    
    Returns:
        dict: Status of supported providers
    """
    status = {}
    
    # Gemini status
    if GEMINI_AVAILABLE:
        try:
            from config import GEMINI_API_KEY
            status["gemini"] = "available" if GEMINI_API_KEY else "no_api_key"
        except Exception:
            status["gemini"] = "error"
    else:
        status["gemini"] = "package_not_installed"

    # OpenAI status
    if OPENAI_AVAILABLE:
        try:
            from config import OPENAI_API_KEY
            status["openai"] = "available" if OPENAI_API_KEY else "no_api_key"
        except Exception:
            status["openai"] = "error"
    else:
        status["openai"] = "package_not_installed"

    # Groq status
    if OPENAI_AVAILABLE:
        try:
            from config import GROQ_API_KEY
            status["groq"] = "available" if GROQ_API_KEY else "no_api_key"
        except Exception:
            status["groq"] = "error"
    else:
        status["groq"] = "package_not_installed"

    return status
