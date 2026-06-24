"""
Demo script for Student AI Travel Planner
This script shows how the app works with sample data without requiring API keys.
"""

import json
from ai_client import _get_dummy_response
from planner import _parse_ai_response, validate_itinerary, calculate_total_cost

def run_demo():
    """Run a demo with sample data."""
    print("🎬 Student AI Travel Planner - Demo")
    print("=" * 50)
    
    # Sample travel request
    destination = "Paris"
    duration = 3
    budget = 200
    interests = ["history", "food"]
    transport = "metro"
    stay = "hostel"
    
    print(f"📍 Destination: {destination}")
    print(f"📅 Duration: {duration} days")
    print(f"💰 Budget: ${budget}")
    print(f"🎯 Interests: {', '.join(interests)}")
    print(f"🚌 Transport: {transport}")
    print(f"🏠 Stay: {stay}")
    print("-" * 50)
    
    # Get dummy response (simulates AI response)
    print("🤖 Generating itinerary...")
    dummy_response = _get_dummy_response()
    
    # Parse the response
    itinerary, summary = _parse_ai_response(dummy_response)
    
    # Display results
    print("✅ Itinerary generated successfully!")
    print()
    
    # Show summary
    print("📋 Trip Summary:")
    print(f"   {summary}")
    print()
    
    # Show cost breakdown
    total_cost = calculate_total_cost(itinerary)
    print("💰 Cost Breakdown:")
    print(f"   Total Estimated Cost: ${total_cost}")
    print(f"   Budget: ${budget}")
    print(f"   Remaining Budget: ${budget - total_cost}")
    print(f"   Average Daily Cost: ${total_cost/len(itinerary):.1f}")
    print()
    
    # Show daily itinerary
    print("📅 Daily Itinerary:")
    for day_data in itinerary:
        print(f"\n   Day {day_data['day']} - ${day_data['cost']}")
        print(f"   🚌 Transport: {day_data['transport']}")
        print(f"   🎯 Activities:")
        for activity in day_data['activities']:
            print(f"      • {activity}")
        print(f"   💡 Notes: {day_data['notes']}")
    
    # Show JSON structure
    print("\n📄 JSON Structure:")
    print("   The itinerary is returned as valid JSON:")
    print(json.dumps({
        "destination": destination,
        "summary": summary,
        "total_cost": total_cost,
        "itinerary": itinerary
    }, indent=2)[:200] + "...")
    
    # Validation check
    print(f"\n✅ Validation:")
    print(f"   Valid structure: {validate_itinerary(itinerary)}")
    print(f"   Number of days: {len(itinerary)}")
    print(f"   Total activities: {sum(len(day['activities']) for day in itinerary)}")

def show_streamlit_demo():
    """Show how to run the Streamlit app."""
    print("\n🌐 Running the Streamlit App:")
    print("-" * 30)
    print("1. Install dependencies:")
    print("   pip install -r requirements.txt")
    print()
    print("2. Add your API keys to config.py:")
    print("   GEMINI_API_KEY = 'your_key_here'")
    print("   # OR")
    print("   OPENAI_API_KEY = 'your_key_here'")
    print()
    print("3. Run the app:")
    print("   streamlit run app.py")
    print()
    print("4. Open your browser to:")
    print("   http://localhost:8501")
    print()
    print("💡 The app will work without API keys (using dummy responses)")
    print("   but will show more realistic results with valid API keys.")

def show_example_prompts():
    """Show example prompts for different scenarios."""
    print("\n📝 Example Prompts:")
    print("-" * 20)
    
    examples = [
        {
            "title": "Budget Backpacker",
            "data": ("Thailand", 7, 300, ["nature", "culture", "food"], "bus", "hostel")
        },
        {
            "title": "City Explorer",
            "data": ("Tokyo", 4, 400, ["technology", "food", "shopping"], "metro", "budget hotel")
        },
        {
            "title": "History Student",
            "data": ("Rome", 5, 250, ["history", "art", "culture"], "walking", "hostel")
        }
    ]
    
    for example in examples:
        title, (dest, days, budget, interests, transport, stay) = example.values()
        print(f"\n   {title}:")
        print(f"   • {dest} for {days} days")
        print(f"   • Budget: ${budget}")
        print(f"   • Interests: {', '.join(interests)}")
        print(f"   • Transport: {transport}")
        print(f"   • Stay: {stay}")

if __name__ == "__main__":
    try:
        run_demo()
        show_streamlit_demo()
        show_example_prompts()
        
        print("\n" + "=" * 50)
        print("🎉 Demo completed successfully!")
        print("💡 Your Student AI Travel Planner is ready to use!")
        
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        print("💡 Check your setup and try again")

