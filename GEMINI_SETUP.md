# 🔑 Gemini API Setup Guide

## 🎯 **Quick Setup (3 Steps)**

### **Step 1: Get Your FREE Gemini API Key**
1. Go to: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the key (starts with `AIza...`)

### **Step 2: Install Required Package**
```bash
pip install google-generativeai
```

### **Step 3: Add Your API Key**
Edit `config.py` and replace the empty key:
```python
GEMINI_API_KEY = "AIzaSyC..."  # Your actual key here
```

## 🚀 **Run the App**
```bash
streamlit run app.py
```

## ✅ **That's It!**

Your Student AI Travel Planner is now ready to use with Google's FREE Gemini AI!

---

## 🧪 **Test Your Setup**

```bash
# Test if everything works
python test_planner.py

# Test Gemini specifically
python test_gemini.py

# Interactive setup (optional)
python setup_gemini.py
```

## 💡 **Benefits of Gemini AI**

- ✅ **Completely FREE** - No credit card required
- ✅ **High Quality** - Google's advanced AI model
- ✅ **Student Friendly** - Perfect for budget travel planning
- ✅ **Easy Setup** - Just one API key needed
- ✅ **Reliable** - Google's infrastructure

## 🔒 **Security Note**

- Keep your API key secret
- Don't share it publicly
- Don't commit it to version control

## 🆘 **Troubleshooting**

**"Package not installed" error:**
```bash
pip install google-generativeai
```

**"API key not set" error:**
- Make sure you added your key to `config.py`
- Check that the key starts with `AIza...`

**App won't start:**
- Make sure Streamlit is installed: `pip install streamlit`
- Try: `streamlit run app.py --server.port 8504`

---

**🎒 Happy Travel Planning with Gemini AI! ✈️**
