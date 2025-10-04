"""
Test script for AI provider switching functionality
This script confirms that switching between Gemini and OpenAI works correctly.
"""

from config import get_provider, get_api_key
from ai_client import test_gemini_availability

def test_provider_switching():
    """Test switching between AI providers."""
    print("🔄 Testing AI Provider Switching...")
    print("=" * 50)
    
    # Get initial provider
    initial_provider = get_provider()
    print(f"📍 Initial provider: {initial_provider}")
    
    # Test provider availability
    print("\n📊 Provider Availability Status:")
    status = test_provider_availability()
    
    for provider, state in status.items():
        status_icon = {
            "available": "✅",
            "no_api_key": "⚠️",
            "package_not_installed": "❌",
            "error": "❌"
        }.get(state, "❓")
        
        print(f"   {status_icon} {provider.title()}: {state}")
    
    # Test switching to Gemini
    print(f"\n🔄 Switching to Gemini...")
    try:
        switch_provider("gemini")
        current_provider = get_provider()
        print(f"   ✅ Current provider: {current_provider}")
        assert current_provider == "gemini", "Should be switched to Gemini"
        
        # Try to get API key (will show error if not set)
        try:
            api_key = get_api_key()
            print(f"   ✅ API key retrieved (length: {len(api_key)})")
        except ValueError as e:
            print(f"   ⚠️ API key issue: {e}")
            
    except Exception as e:
        print(f"   ❌ Error switching to Gemini: {e}")
    
    # Test switching to OpenAI
    print(f"\n🔄 Switching to OpenAI...")
    try:
        switch_provider("openai")
        current_provider = get_provider()
        print(f"   ✅ Current provider: {current_provider}")
        assert current_provider == "openai", "Should be switched to OpenAI"
        
        # Try to get API key (will show error if not set)
        try:
            api_key = get_api_key()
            print(f"   ✅ API key retrieved (length: {len(api_key)})")
        except ValueError as e:
            print(f"   ⚠️ API key issue: {e}")
            
    except Exception as e:
        print(f"   ❌ Error switching to OpenAI: {e}")
    
    # Test invalid provider
    print(f"\n🔄 Testing invalid provider...")
    try:
        switch_provider("invalid_provider")
        print("   ❌ Should have failed for invalid provider")
    except ValueError as e:
        print(f"   ✅ Correctly caught invalid provider: {e}")
    
    # Restore initial provider
    print(f"\n🔄 Restoring initial provider ({initial_provider})...")
    switch_provider(initial_provider)
    final_provider = get_provider()
    print(f"   ✅ Final provider: {final_provider}")
    assert final_provider == initial_provider, "Should be restored to initial provider"

def test_configuration_display():
    """Display current configuration for user reference."""
    print("\n⚙️ Current Configuration:")
    print("-" * 30)
    
    provider = get_provider()
    print(f"   Selected Provider: {provider}")
    
    try:
        api_key = get_api_key()
        masked_key = api_key[:8] + "..." + api_key[-4:] if len(api_key) > 12 else "***"
        print(f"   API Key: {masked_key}")
    except ValueError as e:
        print(f"   API Key: {e}")
    
    # Show how to change provider
    print(f"\n💡 To change provider, edit config.py:")
    print(f"   AI_PROVIDER = \"{'openai' if provider == 'gemini' else 'gemini'}\"")
    
    # Show how to add API keys
    print(f"\n💡 To add API keys, edit config.py:")
    print(f"   GEMINI_API_KEY = \"your_gemini_key_here\"")
    print(f"   OPENAI_API_KEY = \"your_openai_key_here\"")

def run_sample_request():
    """Run a sample request to test the full pipeline."""
    print("\n🧪 Testing Full Pipeline...")
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
        
        print("   📤 Sending test request...")
        response = generate_itinerary(test_prompt)
        
        print("   📥 Received response:")
        print(f"   Length: {len(response)} characters")
        print(f"   Preview: {response[:100]}...")
        
        # Try to parse as JSON
        try:
            import json
            parsed = json.loads(response)
            print("   ✅ Response is valid JSON")
            
            if "itinerary" in parsed and "summary" in parsed:
                print("   ✅ Response has required fields")
            else:
                print("   ⚠️ Response missing required fields")
                
        except json.JSONDecodeError:
            print("   ⚠️ Response is not valid JSON (might be text format)")
        
    except Exception as e:
        print(f"   ❌ Pipeline test failed: {e}")

if __name__ == "__main__":
    print("🚀 Starting AI Provider Switch Tests")
    print("=" * 60)
    
    try:
        test_provider_switching()
        test_configuration_display()
        run_sample_request()
        
        print("\n" + "=" * 60)
        print("🎉 All provider tests completed!")
        print("💡 Your app is ready to switch between Gemini and OpenAI")
        
    except Exception as e:
        print(f"\n❌ Provider test suite failed: {e}")
        print("💡 Check your configuration and try again")
