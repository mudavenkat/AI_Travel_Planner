"""
Quick Start Script for Student AI Travel Planner
This script helps users get started quickly with the app.
"""

import os
import sys

def check_requirements():
    """Check if required packages are installed."""
    print("🔍 Checking Requirements...")
    print("-" * 30)
    
    required_packages = {
        'streamlit': 'Streamlit web framework',
        'google.generativeai': 'Google Gemini AI (optional)',
        'openai': 'OpenAI API (optional)'
    }
    
    missing_packages = []
    
    for package, description in required_packages.items():
        try:
            __import__(package)
            print(f"✅ {package}: Installed")
        except ImportError:
            print(f"❌ {package}: Not installed")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n💡 To install missing packages:")
        print(f"   pip install -r requirements.txt")
        return False
    
    print("\n✅ All required packages are installed!")
    return True

def check_config():
    """Check if configuration is set up."""
    print("\n⚙️ Checking Configuration...")
    print("-" * 30)
    
    try:
        from config import get_provider, get_api_key
        
        provider = get_provider()
        print(f"📍 Selected Provider: {provider}")
        
        try:
            api_key = get_api_key()
            masked_key = api_key[:8] + "..." + api_key[-4:] if len(api_key) > 12 else "***"
            print(f"🔑 API Key: {masked_key}")
            print("✅ Configuration is ready!")
            return True
        except ValueError as e:
            print(f"⚠️ API Key: {e}")
            print("💡 The app will work with dummy responses")
            return False
            
    except ImportError as e:
        print(f"❌ Configuration error: {e}")
        return False

def show_instructions():
    """Show setup instructions."""
    print("\n📋 Setup Instructions:")
    print("-" * 30)
    print("1. Install dependencies:")
    print("   pip install -r requirements.txt")
    print()
    print("2. Add API keys to config.py:")
    print("   # For Gemini (free):")
    print("   GEMINI_API_KEY = 'your_key_here'")
    print()
    print("   # For OpenAI (paid):")
    print("   OPENAI_API_KEY = 'your_key_here'")
    print()
    print("3. Run the app:")
    print("   streamlit run app.py")
    print()
    print("4. Open browser to:")
    print("   http://localhost:8501")

def run_tests():
    """Run basic tests."""
    print("\n🧪 Running Tests...")
    print("-" * 30)
    
    try:
        import subprocess
        result = subprocess.run([sys.executable, "test_planner.py"], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("✅ Basic tests passed!")
            return True
        else:
            print(f"❌ Tests failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Could not run tests: {e}")
        return False

def main():
    """Main quick start function."""
    print("🚀 Student AI Travel Planner - Quick Start")
    print("=" * 50)
    
    # Check requirements
    requirements_ok = check_requirements()
    
    # Check configuration
    config_ok = check_config()
    
    # Show instructions if needed
    if not requirements_ok or not config_ok:
        show_instructions()
    
    # Run tests if everything looks good
    if requirements_ok:
        tests_ok = run_tests()
        
        if tests_ok and config_ok:
            print("\n🎉 Everything is ready!")
            print("💡 Run 'streamlit run app.py' to start the app")
        elif tests_ok:
            print("\n✅ App is ready (with dummy responses)")
            print("💡 Add API keys to config.py for real AI responses")
        else:
            print("\n⚠️ Some issues detected")
            print("💡 Check the error messages above")
    else:
        print("\n❌ Please install requirements first")
        print("💡 Run 'pip install -r requirements.txt'")

if __name__ == "__main__":
    main()
