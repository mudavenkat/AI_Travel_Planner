"""
Currency Feature Demo for Student AI Travel Planner
This script demonstrates the multi-currency support.
"""

from planner import plan_trip

def demo_currencies():
    """Demo different currencies for travel planning."""
    print("💱 Student AI Travel Planner - Currency Feature Demo")
    print("=" * 60)
    print()
    
    # Demo scenarios with different currencies
    demos = [
        {
            "title": "🇺🇸 American Student in Paris",
            "destination": "Paris",
            "duration": 3,
            "budget": 200,
            "currency": "USD",
            "interests": ["history", "food", "culture"],
            "transport": "metro",
            "stay": "hostel"
        },
        {
            "title": "🇪🇺 European Student in Tokyo",
            "destination": "Tokyo", 
            "duration": 4,
            "budget": 150,
            "currency": "EUR",
            "interests": ["technology", "food", "culture"],
            "transport": "train",
            "stay": "hostel"
        },
        {
            "title": "🇯🇵 Japanese Student in Seoul",
            "destination": "Seoul",
            "duration": 3,
            "budget": 200000,
            "currency": "JPY",
            "interests": ["culture", "food", "shopping"],
            "transport": "metro",
            "stay": "hostel"
        },
        {
            "title": "🇮🇳 Indian Student in Bangkok",
            "destination": "Bangkok",
            "duration": 5,
            "budget": 15000,
            "currency": "INR",
            "interests": ["culture", "food", "nature"],
            "transport": "bus",
            "stay": "hostel"
        }
    ]
    
    for i, demo in enumerate(demos, 1):
        print(f"📋 Demo {i}: {demo['title']}")
        print("-" * 50)
        print(f"📍 Destination: {demo['destination']}")
        print(f"📅 Duration: {demo['duration']} days")
        print(f"💰 Budget: {demo['budget']} {demo['currency']}")
        print(f"🎯 Interests: {', '.join(demo['interests'])}")
        print(f"🚌 Transport: {demo['transport']}")
        print(f"🏠 Stay: {demo['stay']}")
        print()
        
        try:
            print("🤖 Generating itinerary...")
            itinerary, summary = plan_trip(
                demo['destination'], demo['duration'], demo['budget'],
                demo['interests'], demo['transport'], demo['stay'], demo['currency']
            )
            
            if isinstance(itinerary, list) and len(itinerary) > 0:
                total_cost = sum(day.get('cost', 0) for day in itinerary)
                print(f"✅ Generated {len(itinerary)}-day itinerary")
                print(f"💰 Total cost: {demo['currency']} {total_cost}")
                print(f"📝 Summary: {summary[:100]}...")
            else:
                print(f"⚠️ Got response: {itinerary}")
                
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print()
        print("=" * 60)
        print()

def show_currency_benefits():
    """Show the benefits of multi-currency support."""
    print("🌟 Benefits of Multi-Currency Support:")
    print("-" * 40)
    print("✅ No more currency conversion confusion")
    print("✅ Local pricing in familiar currency")
    print("✅ Better budget planning for international students")
    print("✅ Realistic cost estimates in local context")
    print("✅ Support for 100+ currencies worldwide")
    print()
    
    print("💡 Popular Currencies Supported:")
    popular_currencies = [
        "USD (US Dollar)", "EUR (Euro)", "GBP (British Pound)",
        "JPY (Japanese Yen)", "AUD (Australian Dollar)", "CAD (Canadian Dollar)",
        "CHF (Swiss Franc)", "CNY (Chinese Yuan)", "INR (Indian Rupee)",
        "BRL (Brazilian Real)", "MXN (Mexican Peso)", "KRW (South Korean Won)",
        "SGD (Singapore Dollar)", "HKD (Hong Kong Dollar)", "NZD (New Zealand Dollar)"
    ]
    
    for currency in popular_currencies:
        print(f"   • {currency}")

if __name__ == "__main__":
    try:
        demo_currencies()
        show_currency_benefits()
        
        print("🎉 Currency feature demo completed!")
        print("💡 Try the web app to see currency selection in action!")
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        print("💡 Make sure your Gemini API key is configured in config.py")







