"""
Test script for Gemini AI functionality
This script tests the Gemini AI integration.
"""

from config import get_provider, get_api_key
from ai_client import test_gemini_availability

def test_gemini_setup():
    """Test Gemini setup and configuration."""
    print("🤖 Testing Gemini AI Setup...")
    print("=" * 40)
    
    # Test provider
    provider = get_provider()
    print(f"📍 Provider: {provider}")
    
    # Test API key
    try:
        api_key = get_api_key()
        masked_key = api_key[:8] + "..." + api_key[-4:]
        print(f"✅ API Key: {masked_key}")
    except ValueError as e:
        print(f"⚠️ API Key: {e}")
    
    # Test availability
    print("\n📊 Gemini Status:")
    status = test_gemini_availability()
    
    for provider, state in status.items():
        if state == "available":
            print(f"✅ {provider.title()}: Ready")
        elif state == "no_api_key":
            print(f"⚠️ {provider.title()}: No API key")
        elif state == "package_not_installed":
            print(f"❌ {provider.title()}: Package not installed")
        else:
            print(f"❌ {provider.title()}: Error")

def test_gemini_request():
    """Test a sample Gemini request."""
    print("\n🧪 Testing Gemini Request...")
    print("-" * 30)
    
    try:
        from ai_client import generate_itinerary
        
        # Simple test prompt
        test_prompt = """
        Create a 1-day student itinerary for Paris with budget $50.
        Focus on history and food interests.
        Use metro transport and hostel accommodation.
        Return valid JSON with itinerary and summary.
        """
        
        print("📤 Sending test request to Gemini...")
        response = generate_itinerary(test_prompt)
        
        print("📥 Received response:")
        print(f"   Length: {len(response)} characters")
        print(f"   Preview: {response[:100]}...")
        
        # Try to parse as JSON
        try:
            import json
            parsed = json.loads(response)
            print("✅ Response is valid JSON")
            
            if "itinerary" in parsed and "summary" in parsed:
                print("✅ Response has required fields")
            else:
                print("⚠️ Response missing required fields")
                
        except json.JSONDecodeError:
            print("⚠️ Response is not valid JSON (might be text format)")
        
    except Exception as e:
        print(f"❌ Request test failed: {e}")

def main():
    """Main test function."""
    print("🚀 Gemini AI Travel Planner - Tests")
    print("=" * 50)
    
    try:
        test_gemini_setup()
        test_gemini_request()
        
        print("\n" + "=" * 50)
        print("🎉 All Gemini tests completed!")
        
    except Exception as e:
        print(f"\n❌ Test suite failed: {e}")

if __name__ == "__main__":
    main()
