"""
Configuration file for Student AI Travel Planner
This file manages the Gemini API key configuration.
"""

# Gemini API Configuration
# Get your free API key from: https://makersuite.google.com/app/apikey
GEMINI_API_KEY = "AIzaSyB2OUiHYfgzC8S5SUsba-9Zrk_T-1spmI8"  # Your Google Gemini API key

def get_provider():
    """
    Returns the AI provider (always Gemini).
    
    Returns:
        str: Always returns "gemini"
    """
    return "gemini"

def get_api_key():
    """
    Returns the Gemini API key.
    
    Returns:
        str: The Gemini API key
        
    Raises:
        ValueError: If no API key is set
    """
    if not GEMINI_API_KEY:
        raise ValueError("Gemini API key not set. Please add your API key to config.py")
    return GEMINI_API_KEY
