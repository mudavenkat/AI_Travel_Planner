"""
Package Installation Script for Student AI Travel Planner
This script helps you install the required packages.
"""

import subprocess
import sys

def install_package(package_name):
    """Install a package using pip."""
    try:
        print(f"📦 Installing {package_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"✅ {package_name} installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {package_name}: {e}")
        return False

def check_package(package_name):
    """Check if a package is installed."""
    try:
        __import__(package_name)
        return True
    except ImportError:
        return False

def main():
    """Main installation function."""
    print("📦 Student AI Travel Planner - Package Installation")
    print("=" * 55)
    print()
    
    # Required packages
    packages = {
        'streamlit': 'streamlit',
        'google.generativeai': 'google-generativeai',
        'openai': 'openai'
    }
    
    print("Checking required packages...")
    print("-" * 30)
    
    missing_packages = []
    
    for import_name, pip_name in packages.items():
        if check_package(import_name):
            print(f"✅ {import_name}: Already installed")
        else:
            print(f"❌ {import_name}: Not installed")
            missing_packages.append(pip_name)
    
    if not missing_packages:
        print("\n🎉 All packages are already installed!")
        return
    
    print(f"\n📦 Need to install: {', '.join(missing_packages)}")
    print()
    
    # Install missing packages
    success_count = 0
    for package in missing_packages:
        if install_package(package):
            success_count += 1
        print()
    
    print("=" * 55)
    if success_count == len(missing_packages):
        print("🎉 All packages installed successfully!")
        print("\n🚀 You can now run the app:")
        print("   streamlit run app.py")
    else:
        print(f"⚠️ {success_count}/{len(missing_packages)} packages installed")
        print("💡 Try installing manually:")
        print("   pip install -r requirements.txt")

if __name__ == "__main__":
    main()

