import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Musafir AI", layout="centered")

# Custom CSS for the logo, button styling, and sidebar background color
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Overpass:wght@400;600&display=swap');
    :root {
        --primary-color: #FF7B02;
        --background-color: #FFFFFF;
        --secondary-background-color: #FF7B02;
        --text-color: #2B2D42;
    }
    [data-testid="stSidebar"] {
        background-color: var(--primary-color) !important;
    }
    body {
        font-family: 'Overpass', sans-serif;
        background-color: var(--background-color);
        color: var(--text-color);
    }
    .title {
        font-size: 2.5em;
        color: var(--primary-color);
        margin-top: 50px;
        text-align: left;
    }
    .subtitle {
        font-size: 1.5em;
        color: var(--primary-color);
        margin-bottom: 40px;
        text-align: left;
    }
    .link-container {
        display: flex;
        justify-content: flex-start;
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
        text-align: center;
        padding: 10px;
        font-size: 0.9em;
    }
    .css-1aumxhk {
        background-color: var(--secondary-background-color) !important;
        color: var(--text-color) !important;
    }
    /* Custom sidebar background color */
    .css-1d391kg {
        background-color: var(--primary-color) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the logo with the theme styling
st.image("logo/musafirlogo.svg", use_column_width=False, width=250)

st.markdown('<div class="title">Musafir AI - Innovative Travel</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Explore and plan your journey with cutting-edge AI technology</div>', unsafe_allow_html=True)

# Interactive Pitch with collapsible sections
with st.expander("What is Musafir AI?"):
    st.markdown("""
    **Musafir AI** is a revolutionary platform designed to empower the Musafir community with AI-powered tools that enhance travel planning and execution. Our suite of applications leverages advanced AI to generate personalized itineraries, create travel checklists, and offer recommendations tailored to individual preferences.
    """)

with st.expander("Can you buy this for your business?"):
    st.markdown("""
    Yes. We offer full integration to your travel ecosystems. Our API's are fast and portable for almost all systems.
    """)

with st.expander("Solving Problems of the Musafir Community"):
    st.markdown("""
    Traveling can be overwhelming, with countless details to manage, from destination research to itinerary planning. Musafir AI simplifies this process by offering automated, yet highly personalized, travel solutions. Whether you're an adventurer seeking the best spots in Hunza or a business traveler needing a precise schedule in Skardu, Musafir AI has you covered.
    """)

with st.expander("Enabling Travel Businesses"):
    st.markdown("""
    For travel businesses, Musafir AI provides an edge in customer service and operational efficiency. By integrating AI-driven tools, travel agencies can offer clients personalized travel plans and checklists, leading to higher satisfaction rates and more repeat business. Musafir AI bridges the gap between technology and hospitality, allowing businesses to thrive in the competitive travel industry.
    """)

# Display buttons that navigate to other pages
#if st.button("Go to Hunza AI"):
 #   st.experimental_set_query_params(page="Free Travel Plans")
#if st.button("Go to Skardu AI"):
 #   st.experimental_set_query_params(page="Free Travel Checklists")

# Footer
st.markdown('<div class="footer">All rights reserved | Created by ADev</div>', unsafe_allow_html=True)
