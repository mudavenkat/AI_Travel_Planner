# ✈️ Student AI Travel Planner

App link:https://aitravelplanner-7bgzksmqm2isy2bdrefmym.streamlit.app/

A beginner-friendly web application that generates personalized, budget-aware travel itineraries for students using AI. The app supports both **Gemini** and **OpenAI** APIs and emphasizes affordability, safety, and ease of use.

## 🌟 Features

- **Student-centered planning**: Budget-friendly options, safety tips, and student discounts
- **Multi-Currency Support**: Choose from 100+ currencies worldwide (USD, EUR, JPY, INR, etc.)
- **Clean Streamlit UI**: Easy-to-use interface with form inputs
- **Structured Output**: Valid JSON itineraries with daily breakdowns
- **Budget Awareness**: Cost tracking and budget optimization in local currency
- **Debug Mode**: Test and troubleshoot without API keys

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- API key for either Gemini or OpenAI (or both)

### Installation

1. **Clone or download** this project to your computer
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure API keys** in `config.py`:
   ```python
   # Edit config.py
   AI_PROVIDER = "gemini"  # or "openai"
   GEMINI_API_KEY = "your_gemini_api_key_here"
   OPENAI_API_KEY = "your_openai_api_key_here"
   ```
4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

### Getting API Keys

#### Gemini API (Free)
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key to `config.py`

#### OpenAI API (Paid)
1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in and create an account
3. Click "Create new secret key"
4. Copy the key to `config.py`

## 📁 Project Structure

```
student-ai-travel-planner/
├── app.py                 # Main Streamlit application
├── config.py             # API keys and provider configuration
├── ai_client.py          # AI provider wrapper (Gemini/OpenAI)
├── planner.py            # Core itinerary generation logic
├── requirements.txt      # Python dependencies
├── test_planner.py       # Basic unit tests
├── test_provider_switch.py # Provider switching tests
└── README.md            # This file
```

## 🧪 Testing

### Run Tests Without API Keys
```bash
python test_planner.py
python test_provider_switch.py
```

### Test with Streamlit Debug Mode
1. Run the app: `streamlit run app.py`
2. Enable "Debug Mode" in the sidebar
3. Submit a test request

## 🎯 How to Use

1. **Open the app** in your browser (usually `http://localhost:8501`)
2. **Fill out the form**:
   - Destination (e.g., "Paris", "Tokyo")
   - Duration in days
   - Budget in your chosen currency
   - Interests (history, food, nature, etc.)
   - Preferred transport
   - Accommodation type
3. **Select your currency** from the dropdown (100+ options available)
4. **Click "Generate My Itinerary"**
5. **Review your personalized plan** with daily activities, costs, and tips
6. **Download as JSON** for offline reference

## 📋 Example Output

```json
{
  "itinerary": [
    {
      "day": 1,
      "activities": [
        "Visit the Eiffel Tower (student discount available)",
        "Explore Montmartre district",
        "Try street food at local markets"
      ],
      "cost": 45,
      "transport": "metro",
      "notes": "Student ID required for discounts. Free walking tour available."
    }
  ],
  "summary": "A fantastic 3-day student adventure in Paris! This budget-friendly itinerary includes iconic landmarks, cultural experiences, and local cuisine."
}
```

## 🔧 Configuration Options

### Switching AI Providers
Edit `config.py`:
```python
AI_PROVIDER = "gemini"    # Switch to "openai" for OpenAI
```

### Customizing the App
- **Interests**: Modify the options in `app.py`
- **Transport types**: Update the selectbox options
- **Accommodation**: Add more options to the dropdown
- **Budget limits**: Adjust validation in `planner.py`

## 🐛 Troubleshooting

### Common Issues

1. **"API key not set" error**
   - Add your API key to `config.py`
   - Make sure the key is correct and active

2. **"Package not installed" error**
   - Run `pip install -r requirements.txt`
   - Check Python version (3.9+ required)

3. **JSON parsing errors**
   - Enable debug mode to see raw AI response
   - Try switching AI providers
   - Check if API key has sufficient credits

4. **App won't start**
   - Check if Streamlit is installed: `pip install streamlit`
   - Try running: `streamlit run app.py --server.port 8502`

### Debug Mode
Enable debug mode in the Streamlit sidebar to see:
- Current AI provider
- Raw AI responses
- Provider availability status
- Detailed error messages

## 🎓 Educational Use

This project is designed for educational purposes and includes:
- **Clear comments** explaining each step
- **Modular structure** for easy understanding
- **Error handling** with helpful messages
- **Testing framework** for learning
- **Beginner-friendly** code organization

Perfect for:
- Computer Science classes
- AI/ML workshops
- Web development tutorials
- API integration lessons

## 🤝 Contributing

Feel free to:
- Add new features
- Improve the UI/UX
- Add more AI providers
- Enhance error handling
- Write additional tests

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Enable debug mode for detailed error messages
3. Run the test scripts to verify setup
4. Check your API key status and credits

---

**Happy Travel Planning! ✈️🎒**
