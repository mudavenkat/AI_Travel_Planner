"""
API Key Setup Script for Student AI Travel Planner
This script helps you configure your API keys easily.
"""

import os

def setup_gemini_key():
    """Setup Gemini API key."""
    print("🔑 Setting up Gemini API Key")
    print("-" * 40)
    print("1. Go to: https://makersuite.google.com/app/apikey")
    print("2. Sign in with your Google account")
    print("3. Click 'Create API Key'")
    print("4. Copy the key (starts with 'AIza...')")
    print()
    
    key = input("Paste your Gemini API key here: ").strip()
    
    if key and key.startswith('AIza'):
        return key
    else:
        print("❌ Invalid key format. Gemini keys start with 'AIza...'")
        return None

def setup_openai_key():
    """Setup OpenAI API key."""
    print("🔑 Setting up OpenAI API Key")
    print("-" * 40)
    print("1. Go to: https://platform.openai.com/api-keys")
    print("2. Sign in and add payment method")
    print("3. Click 'Create new secret key'")
    print("4. Copy the key (starts with 'sk-...')")
    print()
    
    key = input("Paste your OpenAI API key here: ").strip()
    
    if key and key.startswith('sk-'):
        return key
    else:
        print("❌ Invalid key format. OpenAI keys start with 'sk-...'")
        return None

def update_config_file(gemini_key=None, openai_key=None, provider="gemini"):
    """Update the config.py file with new API keys."""
    
    # Read current config
    try:
        with open('config.py', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("❌ config.py not found!")
        return False
    
    # Update Gemini key
    if gemini_key:
        if 'GEMINI_API_KEY = ""' in content:
            content = content.replace('GEMINI_API_KEY = ""', f'GEMINI_API_KEY = "{gemini_key}"')
        else:
            # Find and replace existing key
            import re
            content = re.sub(r'GEMINI_API_KEY = "[^"]*"', f'GEMINI_API_KEY = "{gemini_key}"', content)
    
    # Update OpenAI key
    if openai_key:
        if 'OPENAI_API_KEY = ""' in content:
            content = content.replace('OPENAI_API_KEY = ""', f'OPENAI_API_KEY = "{openai_key}"')
        else:
            # Find and replace existing key
            import re
            content = re.sub(r'OPENAI_API_KEY = "[^"]*"', f'OPENAI_API_KEY = "{openai_key}"', content)
    
    # Update provider
    if provider:
        import re
        content = re.sub(r'AI_PROVIDER = "[^"]*"', f'AI_PROVIDER = "{provider}"', content)
    
    # Write updated config
    try:
        with open('config.py', 'w') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"❌ Error writing config.py: {e}")
        return False

def main():
    """Main setup function."""
    print("🚀 Student AI Travel Planner - API Key Setup")
    print("=" * 50)
    print()
    
    print("Choose your AI provider:")
    print("1. Gemini (FREE) - Recommended for students")
    print("2. OpenAI (PAID) - More advanced responses")
    print("3. Both (you can switch between them)")
    print()
    
    choice = input("Enter your choice (1, 2, or 3): ").strip()
    
    gemini_key = None
    openai_key = None
    provider = "gemini"
    
    if choice == "1":
        print("\n🎯 Setting up Gemini (FREE)")
        gemini_key = setup_gemini_key()
        provider = "gemini"
        
    elif choice == "2":
        print("\n🎯 Setting up OpenAI (PAID)")
        openai_key = setup_openai_key()
        provider = "openai"
        
    elif choice == "3":
        print("\n🎯 Setting up both providers")
        gemini_key = setup_gemini_key()
        print()
        openai_key = setup_openai_key()
        provider = "gemini"  # Default to Gemini
        
    else:
        print("❌ Invalid choice!")
        return
    
    # Update config file
    if gemini_key or openai_key:
        print(f"\n💾 Updating config.py...")
        if update_config_file(gemini_key, openai_key, provider):
            print("✅ Configuration updated successfully!")
            
            # Show what was configured
            if gemini_key:
                masked_key = gemini_key[:8] + "..." + gemini_key[-4:]
                print(f"✅ Gemini key configured: {masked_key}")
            
            if openai_key:
                masked_key = openai_key[:8] + "..." + openai_key[-4:]
                print(f"✅ OpenAI key configured: {masked_key}")
            
            print(f"✅ Default provider: {provider}")
            
            print(f"\n🚀 You're all set! Run the app:")
            print(f"   streamlit run app.py")
            
        else:
            print("❌ Failed to update configuration")
    else:
        print("❌ No valid API keys provided")

def test_api_keys():
    """Test if API keys are working."""
    print("\n🧪 Testing API Keys...")
    print("-" * 30)
    
    try:
        from ai_client import test_provider_availability
        
        status = test_provider_availability()
        
        for provider, state in status.items():
            if state == "available":
                print(f"✅ {provider.title()}: Working")
            elif state == "no_api_key":
                print(f"⚠️ {provider.title()}: No API key")
            elif state == "package_not_installed":
                print(f"❌ {provider.title()}: Package not installed")
            else:
                print(f"❌ {provider.title()}: Error")
                
    except Exception as e:
        print(f"❌ Error testing API keys: {e}")

if __name__ == "__main__":
    main()
    
    # Ask if user wants to test
    test_choice = input("\n🧪 Test your API keys? (y/n): ").strip().lower()
    if test_choice == 'y':
        test_api_keys()
