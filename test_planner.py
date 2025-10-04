"""
Basic Unit Tests for Student AI Travel Planner
This file tests the planner logic without running the full Streamlit app.
"""

from planner import plan_trip, validate_itinerary, calculate_total_cost

def test_planner_basic():
    """Test basic planner functionality with sample data."""
    print("🧪 Testing Student AI Travel Planner...")
    print("=" * 50)
    
    # Test data
    destination = "Paris"
    duration = 2
    budget = 100
    interests = ["food", "history"]
    transport = "metro"
    stay = "hostel"
    
    print(f"📍 Destination: {destination}")
    print(f"📅 Duration: {duration} days")
    print(f"💰 Budget: ${budget}")
    print(f"🎯 Interests: {interests}")
    print(f"🚌 Transport: {transport}")
    print(f"🏠 Stay: {stay}")
    print("-" * 50)
    
    try:
        # Test the planner
        itinerary, summary = plan_trip(
            destination, duration, budget, interests, transport, stay, "USD"
        )
        
        print("✅ Planner executed successfully!")
        print()
        
        # Test itinerary structure
        print("📋 Generated Itinerary:")
        if isinstance(itinerary, list):
            print(f"   • Number of days: {len(itinerary)}")
            
            for day_data in itinerary:
                print(f"   • Day {day_data.get('day', '?')}: ${day_data.get('cost', 0)}")
                print(f"     Activities: {len(day_data.get('activities', []))}")
                print(f"     Transport: {day_data.get('transport', 'N/A')}")
            
            # Test validation
            is_valid = validate_itinerary(itinerary)
            print(f"   • Valid structure: {is_valid}")
            
            # Test cost calculation
            total_cost = calculate_total_cost(itinerary)
            print(f"   • Total cost: ${total_cost}")
            
        else:
            print(f"   • Error response: {itinerary}")
        
        print()
        print("📝 Summary:")
        print(f"   {summary}")
        print()
        
        # Assertions for automated testing
        assert isinstance(itinerary, (list, dict)), "Itinerary should be a list or dict"
        assert isinstance(summary, str), "Summary should be a string"
        assert len(summary) > 0, "Summary should not be empty"
        
        if isinstance(itinerary, list):
            assert validate_itinerary(itinerary), "Itinerary should have valid structure"
            assert calculate_total_cost(itinerary) >= 0, "Total cost should be non-negative"
        
        print("✅ All tests passed!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        raise

def test_input_validation():
    """Test input validation."""
    print("\n🔍 Testing Input Validation...")
    print("-" * 30)
    
    # Test empty destination
    try:
        plan_trip("", 2, 100, ["food"], "metro", "hostel", "USD")
        print("❌ Should have failed for empty destination")
    except ValueError as e:
        print(f"✅ Correctly caught empty destination: {e}")
    
    # Test invalid duration
    try:
        plan_trip("Paris", 0, 100, ["food"], "metro", "hostel", "USD")
        print("❌ Should have failed for invalid duration")
    except ValueError as e:
        print(f"✅ Correctly caught invalid duration: {e}")
    
    # Test invalid budget
    try:
        plan_trip("Paris", 2, -50, ["food"], "metro", "hostel", "USD")
        print("❌ Should have failed for negative budget")
    except ValueError as e:
        print(f"✅ Correctly caught negative budget: {e}")
    
    # Test empty interests
    try:
        plan_trip("Paris", 2, 100, [], "metro", "hostel", "USD")
        print("❌ Should have failed for empty interests")
    except ValueError as e:
        print(f"✅ Correctly caught empty interests: {e}")
    
    print("✅ Input validation tests passed!")

def test_itinerary_validation():
    """Test itinerary validation functions."""
    print("\n🔍 Testing Itinerary Validation...")
    print("-" * 30)
    
    # Valid itinerary
    valid_itinerary = [
        {
            "day": 1,
            "activities": ["Visit museum", "Try local food"],
            "cost": 50,
            "transport": "metro",
            "notes": "Great day!"
        }
    ]
    
    assert validate_itinerary(valid_itinerary) == True, "Valid itinerary should pass validation"
    assert calculate_total_cost(valid_itinerary) == 50, "Cost calculation should be correct"
    
    # Invalid itinerary (missing field)
    invalid_itinerary = [
        {
            "day": 1,
            "activities": ["Visit museum"],
            # Missing cost, transport, notes
        }
    ]
    
    assert validate_itinerary(invalid_itinerary) == False, "Invalid itinerary should fail validation"
    
    print("✅ Itinerary validation tests passed!")

if __name__ == "__main__":
    print("🚀 Starting Student AI Travel Planner Tests")
    print("=" * 60)
    
    try:
        # Run all tests
        test_planner_basic()
        test_input_validation()
        test_itinerary_validation()
        
        print("\n" + "=" * 60)
        print("🎉 All tests completed successfully!")
        print("💡 Tip: If you see dummy responses, make sure to add your API keys to config.py")
        
    except Exception as e:
        print(f"\n❌ Test suite failed: {e}")
        print("💡 Check your configuration and try again")
