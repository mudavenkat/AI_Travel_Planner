"""
Travel Planner Logic for Student AI Travel Planner
This module handles the core logic for generating travel itineraries.
"""

import json
import re
from ai_client import generate_itinerary

def plan_trip(destination, duration, budget, interests, transport, stay, currency="USD"):
    """
    Generate a personalized travel itinerary for students.
    
    Args:
        destination (str): Travel destination
        duration (int): Number of days
        budget (float): Budget in specified currency
        interests (list): List of interests (e.g., ['history', 'food', 'nature'])
        transport (str): Preferred transport method
        stay (str): Preferred accommodation type
        currency (str): Currency code (e.g., 'USD', 'EUR', 'JPY')
        
    Returns:
        tuple: (itinerary_dict, summary_string)
        
    Raises:
        ValueError: If inputs are invalid
    """
    # Input validation
    if not destination or not destination.strip():
        raise ValueError("Destination cannot be empty")
    
    if not isinstance(duration, int) or duration <= 0:
        raise ValueError("Duration must be a positive integer")
    
    if not isinstance(budget, (int, float)) or budget <= 0:
        raise ValueError("Budget must be a positive number")
    
    if not interests or len(interests) == 0:
        raise ValueError("At least one interest must be selected")
    
    # Create the prompt for the AI
    prompt = _create_prompt(destination, duration, budget, interests, transport, stay, currency)
    
    # Generate itinerary using AI
    try:
        ai_response = generate_itinerary(prompt)
        itinerary_dict, summary = _parse_ai_response(ai_response)
        return itinerary_dict, summary
    except Exception as e:
        # Return error-friendly response
        error_itinerary = {
            "error": str(e),
            "suggestion": "Please check your API keys in config.py or try again later."
        }
        error_summary = f"Unable to generate itinerary: {e}. Please check your configuration and try again."
        return error_itinerary, error_summary

def _create_prompt(destination, duration, budget, interests, transport, stay, currency):
    """
    Create a detailed prompt for the AI to generate a student-focused itinerary.
    
    Args:
        destination (str): Travel destination
        duration (int): Number of days
        budget (float): Budget in specified currency
        interests (list): List of interests
        transport (str): Preferred transport method
        stay (str): Preferred accommodation type
        currency (str): Currency code
        
    Returns:
        str: Formatted prompt for AI
    """
    interests_str = ", ".join(interests)
    
    prompt = f"""
You are an expert travel planner specializing in budget-friendly student travel. Create a detailed itinerary for a student trip with the following requirements:

DESTINATION: {destination}
DURATION: {duration} days
BUDGET: {budget} {currency} total
INTERESTS: {interests_str}
TRANSPORT: {transport}
ACCOMMODATION: {stay}

REQUIREMENTS FOR STUDENT TRAVEL:
1. Prioritize budget-friendly options (public transport, hostels, local food, free activities)
2. Include safety tips relevant to student travelers
3. Suggest student discounts and free activities
4. Recommend affordable local restaurants and street food
5. Include practical tips for first-time travelers

OUTPUT FORMAT:
Please provide your response as valid JSON with this exact structure:

{{
    "itinerary": [
        {{
            "day": 1,
            "activities": ["Activity 1", "Activity 2", "Activity 3"],
            "cost": 50,
            "transport": "metro/bus/walking",
            "notes": "Important tips and safety notes"
        }}
    ],
    "summary": "A concise 2-3 sentence summary of the trip, highlighting key experiences and budget considerations for students."
}}

IMPORTANT:
- Ensure the JSON is valid and properly formatted
- Keep total daily costs reasonable for student budgets
- Include practical safety and money-saving tips
- Suggest free activities and student discounts where possible
- Make it engaging and exciting for young travelers
- Include cultural experiences and local insights
"""
    return prompt

def _parse_ai_response(ai_response):
    """
    Parse the AI response to extract itinerary and summary.
    
    Args:
        ai_response (str): Raw response from AI
        
    Returns:
        tuple: (itinerary_dict, summary_string)
    """
    try:
        # Try to parse as JSON directly
        data = json.loads(ai_response)
        
        if "itinerary" in data and "summary" in data:
            return data["itinerary"], data["summary"]
        else:
            raise ValueError("Response missing required 'itinerary' or 'summary' fields")
            
    except json.JSONDecodeError:
        # If direct JSON parsing fails, try to extract JSON from the response
        try:
            # Look for JSON block in the response
            json_match = re.search(r'\{.*\}', ai_response, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                data = json.loads(json_str)
                
                if "itinerary" in data and "summary" in data:
                    return data["itinerary"], data["summary"]
            
            # If no JSON found, create a fallback response
            fallback_itinerary = [
                {
                    "day": 1,
                    "activities": ["AI response parsing failed - please try again"],
                    "cost": 0,
                    "transport": "N/A",
                    "notes": "There was an issue processing the AI response. Please check your configuration."
                }
            ]
            fallback_summary = "Unable to parse AI response. Please check your API configuration and try again."
            return fallback_itinerary, fallback_summary
            
        except Exception as e:
            # Ultimate fallback
            error_itinerary = [
                {
                    "day": 1,
                    "activities": [f"Error: {str(e)}"],
                    "cost": 0,
                    "transport": "N/A",
                    "notes": "Please check your API keys and configuration."
                }
            ]
            error_summary = f"Error processing response: {str(e)}"
            return error_itinerary, error_summary

def validate_itinerary(itinerary):
    """
    Validate that an itinerary has the required structure.
    
    Args:
        itinerary: The itinerary to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(itinerary, list):
        return False
    
    for day in itinerary:
        if not isinstance(day, dict):
            return False
        
        required_fields = ["day", "activities", "cost", "transport", "notes"]
        if not all(field in day for field in required_fields):
            return False
        
        if not isinstance(day["activities"], list) or len(day["activities"]) == 0:
            return False
        
        if not isinstance(day["cost"], (int, float)) or day["cost"] < 0:
            return False
    
    return True

def calculate_total_cost(itinerary):
    """
    Calculate the total estimated cost for the itinerary.
    
    Args:
        itinerary (list): List of daily itineraries
        
    Returns:
        float: Total estimated cost
    """
    if not validate_itinerary(itinerary):
        return 0
    
    total = sum(day.get("cost", 0) for day in itinerary)
    return round(total, 2)
