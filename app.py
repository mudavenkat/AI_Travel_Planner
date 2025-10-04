"""
Student AI Travel Planner - Streamlit Interface
A beginner-friendly web app for generating personalized travel itineraries.
"""

import streamlit as st
import json
from planner import plan_trip, validate_itinerary, calculate_total_cost
from config import get_provider
from ai_client import test_gemini_availability

# Page configuration
st.set_page_config(
    page_title="Student AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """Main application function."""
    
    # Header
    st.title("✈️ Student AI Travel Planner")
    st.markdown("""
    **Generate personalized, budget-friendly travel itineraries tailored for students!**
    
    This app uses AI to create detailed travel plans that prioritize affordability, safety, and student-friendly experiences.
    """)
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # AI Provider Info
        st.subheader("AI Provider")
        current_provider = get_provider()
        st.info(f"🤖 Using **{current_provider.title()}** AI (Google's free AI service)")
        
        # Debug Mode
        debug_mode = st.checkbox(
            "🐛 Enable Debug Mode",
            help="Show raw AI responses and provider status"
        )
        
        # Provider Status
        if debug_mode:
            st.subheader("Gemini Status")
            status = test_gemini_availability()
            
            for provider, state in status.items():
                if state == "available":
                    st.success(f"✅ {provider.title()}: Ready")
                elif state == "no_api_key":
                    st.warning(f"⚠️ {provider.title()}: No API key")
                elif state == "package_not_installed":
                    st.error(f"❌ {provider.title()}: Package not installed")
                else:
                    st.error(f"❌ {provider.title()}: Error")
    
    # Main form
    st.header("📝 Plan Your Trip")
    
    with st.form("travel_planning_form"):
        # Create two columns for better layout
        col1, col2 = st.columns(2)
        
        with col1:
            destination = st.text_input(
                "🏙️ Destination",
                placeholder="e.g., Paris, Tokyo, New York",
                help="Enter your travel destination"
            )
            
            duration = st.number_input(
                "📅 Duration (days)",
                min_value=1,
                max_value=30,
                value=3,
                help="Number of days for your trip"
            )
            
            # Currency and Budget
            col_budget1, col_budget2 = st.columns([1, 2])
            
            with col_budget1:
                currency = st.selectbox(
                    "💱 Currency",
                    options=[
                        "USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", 
                        "INR", "BRL", "MXN", "KRW", "SGD", "HKD", "NZD", "SEK", 
                        "NOK", "DKK", "PLN", "CZK", "HUF", "TRY", "RUB", "ZAR",
                        "AED", "SAR", "QAR", "KWD", "BHD", "OMR", "JOD", "LBP",
                        "EGP", "MAD", "TND", "DZD", "LYD", "SDG", "ETB", "KES",
                        "UGX", "TZS", "MWK", "ZMW", "BWP", "NAD", "SZL", "LSL",
                        "MUR", "SCR", "MVR", "PKR", "BDT", "LKR", "NPR", "AFN",
                        "KZT", "UZS", "KGS", "TJS", "TMT", "AZN", "AMD", "GEL",
                        "BYN", "MDL", "UAH", "RON", "BGN", "HRK", "RSD", "MKD",
                        "ALL", "BAM", "XOF", "XAF", "XPF", "THB", "VND", "IDR",
                        "MYR", "PHP", "MMK", "LAK", "KHR", "BND", "FJD", "PGK",
                        "SBD", "VUV", "WST", "TOP", "NIO", "GTQ", "HNL", "SVC",
                        "PAB", "CRC", "BZD", "JMD", "TTD", "BBD", "XCD", "AWG",
                        "ANG", "SRD", "GYD", "BOB", "CLP", "ARS", "UYU", "PYG",
                        "COP", "PEN", "VES", "DOP", "HTG", "CUP", "CUC"
                    ],
                    index=0,
                    help="Select your local currency"
                )
            
            with col_budget2:
                budget = st.number_input(
                    f"💰 Budget ({currency})",
                    min_value=1.0,
                    value=200.0 if currency == "USD" else 150.0,
                    step=10.0,
                    help=f"Total budget for your trip in {currency}"
                )
        
        with col2:
            interests = st.multiselect(
                "🎯 Interests",
                options=[
                    "history", "culture", "food", "nature", 
                    "nightlife", "shopping", "art", "adventure",
                    "photography", "music", "sports", "beaches"
                ],
                default=["history", "food"],
                help="Select your interests to personalize the itinerary"
            )
            
            transport = st.selectbox(
                "🚌 Preferred Transport",
                options=["metro/subway", "bus", "train", "rideshare", "walking", "mixed"],
                index=0,
                help="Your preferred mode of transportation"
            )
            
            stay = st.selectbox(
                "🏠 Accommodation Type",
                options=["hostel", "homestay", "budget hotel", "airbnb", "couchsurfing"],
                index=0,
                help="Type of accommodation you prefer"
            )
        
        # Submit button
        submitted = st.form_submit_button(
            "🚀 Generate My Itinerary",
            type="primary",
            use_container_width=True
        )
    
    # Process form submission
    if submitted:
        if not destination:
            st.error("❌ Please enter a destination!")
        elif not interests:
            st.error("❌ Please select at least one interest!")
        else:
            # Show loading spinner
            with st.spinner("🤖 AI is planning your perfect student trip..."):
                try:
                    # Generate itinerary
                    itinerary, summary = plan_trip(
                        destination, duration, budget, interests, transport, stay, currency
                    )
                    
                    # Display results
                    display_results(itinerary, summary, debug_mode, destination, currency)
                    
                except Exception as e:
                    st.error(f"❌ Error generating itinerary: {str(e)}")
                    st.info("💡 Tip: Check your API keys in config.py or enable debug mode for more details.")

def display_results(itinerary, summary, debug_mode=False, destination="Unknown", currency="USD"):
    """Display the generated itinerary and summary."""
    
    st.header("🗺️ Your Personalized Itinerary")
    
    # Check if itinerary is valid
    if isinstance(itinerary, dict) and "error" in itinerary:
        st.error(f"❌ {itinerary['error']}")
        st.info(f"💡 {itinerary.get('suggestion', 'Please try again later.')}")
        return
    
    # Validate itinerary structure
    if not validate_itinerary(itinerary):
        st.error("❌ Invalid itinerary format received from AI")
        if debug_mode:
            st.json(itinerary)
        return
    
    # Calculate total cost
    total_cost = calculate_total_cost(itinerary)
    
    # Display summary
    st.subheader("📋 Trip Summary")
    st.success(summary)
    
    # Cost breakdown
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Estimated Cost", f"{currency} {total_cost}")
    with col2:
        st.metric("Days", len(itinerary))
    with col3:
        st.metric("Avg Daily Cost", f"{currency} {total_cost/len(itinerary):.1f}")
    
    # Display daily itinerary
    st.subheader("📅 Daily Breakdown")
    
    for day_data in itinerary:
        with st.expander(f"Day {day_data['day']} - {currency} {day_data['cost']}"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write("**Activities:**")
                for activity in day_data['activities']:
                    st.write(f"• {activity}")
                
                st.write("**Notes:**")
                st.info(day_data['notes'])
            
            with col2:
                st.write("**Transport:**")
                st.write(f"🚌 {day_data['transport']}")
                
                st.write("**Daily Cost:**")
                st.write(f"💰 {currency} {day_data['cost']}")
    
    # Debug information
    if debug_mode:
        st.subheader("🐛 Debug Information")
        st.write("**Current Provider:**", get_provider())
        st.write("**Raw Itinerary Data:**")
        st.json(itinerary)
    
    # Download button for itinerary
    st.subheader("💾 Download Your Itinerary")
    
    # Create downloadable JSON
    itinerary_json = json.dumps({
        "destination": destination,
        "currency": currency,
        "summary": summary,
        "total_cost": total_cost,
        "itinerary": itinerary
    }, indent=2)
    
    st.download_button(
        label="📥 Download as JSON",
        data=itinerary_json,
        file_name=f"travel_itinerary_{destination.replace(' ', '_').lower()}.json",
        mime="application/json"
    )

def show_example():
    """Show an example itinerary."""
    st.header("📖 Example Itinerary")
    st.markdown("""
    Here's an example of what your itinerary might look like:
    """)
    
    example_itinerary = [
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
        },
        {
            "day": 2,
            "activities": [
                "Louvre Museum (free for EU students under 26)",
                "Walk along the Seine River",
                "Visit Notre-Dame Cathedral (exterior only)"
            ],
            "cost": 25,
            "transport": "metro + walking",
            "notes": "Book Louvre tickets online to skip queues."
        }
    ]
    
    example_summary = "A fantastic 2-day student adventure in Paris! This budget-friendly itinerary includes iconic landmarks and cultural experiences with efficient metro transport and student discounts."
    
    # Display example without expanders to avoid nesting issues
    display_example_results(example_itinerary, example_summary, "Paris", "USD")

def display_example_results(itinerary, summary, destination="Example", currency="USD"):
    """Display example results without expanders to avoid nesting issues."""
    
    # Display summary
    st.subheader("📋 Example Trip Summary")
    st.success(summary)
    
    # Calculate total cost
    total_cost = calculate_total_cost(itinerary)
    
    # Cost breakdown
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Estimated Cost", f"{currency} {total_cost}")
    with col2:
        st.metric("Days", len(itinerary))
    with col3:
        st.metric("Avg Daily Cost", f"{currency} {total_cost/len(itinerary):.1f}")
    
    # Display daily itinerary without expanders
    st.subheader("📅 Example Daily Breakdown")
    
    for day_data in itinerary:
        st.markdown(f"### Day {day_data['day']} - {currency} {day_data['cost']}")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.write("**Activities:**")
            for activity in day_data['activities']:
                st.write(f"• {activity}")
            
            st.write("**Notes:**")
            st.info(day_data['notes'])
        
        with col2:
            st.write("**Transport:**")
            st.write(f"🚌 {day_data['transport']}")
            
            st.write("**Daily Cost:**")
            st.write(f"💰 {currency} {day_data['cost']}")
        
        st.markdown("---")

if __name__ == "__main__":
    # Add example section
    with st.expander("📖 See Example Itinerary"):
        show_example()
    
    # Run main app
    main()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Built with ❤️ for students | Powered by AI | 
        <a href='#'>GitHub</a> | <a href='#'>Documentation</a></p>
    </div>
    """, unsafe_allow_html=True)
