"""
AI Client wrapper for Student AI Travel Planner
This module handles communication with the Gemini API.
"""

import json
from config import get_api_key

# Import Gemini library (with error handling for missing package)
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("Warning: google-generativeai not installed. Install with: pip install google-generativeai")

def generate_itinerary(prompt: str) -> str:
    """
    Generate travel itinerary using the Gemini API.
    
    Args:
        prompt (str): The prompt containing travel details and requirements
        
    Returns:
        str: Raw AI response containing the itinerary
        
    Raises:
        Exception: If API call fails or Gemini is not available
    """
    api_key = get_api_key()
    
    # Check if required package is installed
    if not GEMINI_AVAILABLE:
        raise Exception("Gemini requires 'google-generativeai' package. Install with: pip install google-generativeai")
    
    try:
        return _call_gemini(prompt, api_key)
    except Exception as e:
        # Return dummy response for testing when no API key is available
        if "API key not set" in str(e):
            print(f"Warning: {e}. Using dummy response for testing.")
            return _get_dummy_response()
        raise e

def _call_gemini(prompt: str, api_key: str) -> str:
    """
    Call Google Gemini API.
    
    Args:
        prompt (str): The prompt to send
        api_key (str): Gemini API key
        
    Returns:
        str: Gemini response
    """
    # Configure Gemini
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    # Generate response
    response = model.generate_content(prompt)
    return response.text


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

def test_gemini_availability():
    """
    Test if Gemini is available and properly configured.
    
    Returns:
        dict: Status of Gemini provider
    """
    status = {}
    
    # Test Gemini
    if GEMINI_AVAILABLE:
        try:
            from config import GEMINI_API_KEY
            status["gemini"] = "available" if GEMINI_API_KEY else "no_api_key"
        except:
            status["gemini"] = "error"
    else:
        status["gemini"] = "package_not_installed"
    
    return status
