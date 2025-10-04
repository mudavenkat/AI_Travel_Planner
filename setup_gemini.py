"""
Simple Gemini API Setup Script for Student AI Travel Planner
This script helps you set up your Gemini API key quickly.
"""

def setup_gemini_key():
    """Setup Gemini API key."""
    print("🔑 Gemini API Setup (FREE)")
    print("=" * 40)
    print()
    print("📋 Steps to get your FREE Gemini API key:")
    print("1. Go to: https://makersuite.google.com/app/apikey")
    print("2. Sign in with your Google account")
    print("3. Click 'Create API Key'")
    print("4. Copy the key (starts with 'AIza...')")
    print()
    
    key = input("🔑 Paste your Gemini API key here: ").strip()
    
    if key and key.startswith('AIza'):
        # Update config.py
        try:
            with open('config.py', 'r') as f:
                content = f.read()
            
            # Replace the empty API key
            content = content.replace('GEMINI_API_KEY = ""', f'GEMINI_API_KEY = "{key}"')
            
            with open('config.py', 'w') as f:
                f.write(content)
            
            print()
            print("✅ API key saved successfully!")
            print("🚀 You can now run the app:")
            print("   streamlit run app.py")
            
        except Exception as e:
            print(f"❌ Error saving API key: {e}")
            print("💡 Please manually edit config.py and add your key")
    
    else:
        print("❌ Invalid key format. Gemini keys start with 'AIza...'")
        print("💡 Please check your key and try again")

def test_setup():
    """Test if the setup is working."""
    print("\n🧪 Testing Setup...")
    print("-" * 20)
    
    try:
        from config import get_api_key, get_provider
        
        provider = get_provider()
        print(f"✅ Provider: {provider}")
        
        api_key = get_api_key()
        masked_key = api_key[:8] + "..." + api_key[-4:]
        print(f"✅ API Key: {masked_key}")
        
        print("\n🎉 Setup is complete! Your app is ready to use.")
        
    except ValueError as e:
        print(f"⚠️ {e}")
        print("💡 Run this script again to add your API key")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Main setup function."""
    print("🚀 Student AI Travel Planner - Gemini Setup")
    print("=" * 50)
    print()
    print("This app uses Google's FREE Gemini AI to generate")
    print("personalized travel itineraries for students.")
    print()
    
    # Check current status
    try:
        from config import get_api_key
        api_key = get_api_key()
        print("✅ API key is already configured!")
        test_setup()
    except ValueError:
        print("⚠️ No API key found. Let's set it up!")
        print()
        setup_gemini_key()

if __name__ == "__main__":
    main()
