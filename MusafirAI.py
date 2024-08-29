import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Musafir AI", layout="centered")

# Custom CSS for the design system, sidebar, and logo
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Overpass:wght@400;600&display=swap');

    body {
        font-family: 'Overpass', sans-serif;
        background-color: #2B2D42;
        color: #FA3E01;
    }
    .title {
        font-size: 2.5em;
        color: #FA3E01;
        text-align: center;
        margin-top: 50px;
    }
    .subtitle {
        font-size: 1.5em;
        text-align: center;
        margin-bottom: 40px;
        color: #FF7B02;
    }
    .link-container {
        display: flex;
        justify-content: center;
        margin-top: 40px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #FF490E 0%, #FF7B02 100%) !important;
        border: none;
        color: white;
        padding: 15px 30px;
        text-align: center;
        display: inline-block;
        font-size: 16px;
        cursor: pointer;
        border-radius: 8px;
        margin: 0 10px;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0F1116;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 0.9em;
    }
    /* Sidebar customization */
    .css-1d391kg {
        background: linear-gradient(90deg, #FF490E 0%, #FF7B02 100%) !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the logo
st.image("logo/musafirlogo.png", use_column_width=False, width=100)

st.markdown('<div class="title">Musafir AI - Innovative Travel</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Explore and plan your journey with cutting-edge AI technology</div>', unsafe_allow_html=True)

# Interactive Pitch
st.markdown("""
### What is Musafir AI?

**Musafir AI** is a revolutionary platform designed to empower the Musafir (traveler) community with AI-powered tools that enhance travel planning and execution. Our suite of applications leverages advanced AI to generate personalized itineraries, create travel checklists, and offer recommendations tailored to individual preferences.

### Solving Problems of the Musafir Community

Traveling can be overwhelming, with countless details to manage, from destination research to itinerary planning. Musafir AI simplifies this process by offering automated, yet highly personalized, travel solutions. Whether you're an adventurer seeking the best spots in Hunza or a business traveler needing a precise schedule in Skardu, Musafir AI has you covered.

### Enabling Travel Businesses

For travel businesses, Musafir AI provides an edge in customer service and operational efficiency. By integrating AI-driven tools, travel agencies can offer clients personalized travel plans and checklists, leading to higher satisfaction rates and more repeat business. Musafir AI bridges the gap between technology and hospitality, allowing businesses to thrive in the competitive travel industry.
""")

# Display buttons that navigate to other pages
if st.button("Go to Hunza AI"):
    st.experimental_set_query_params(page="HunzaAI")
if st.button("Go to Skardu AI"):
    st.experimental_set_query_params(page="SkarduAI")

# Footer
st.markdown('<div class="footer">All rights reserved | Created by ADev</div>', unsafe_allow_html=True)
