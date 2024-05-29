import streamlit as st
from cohere_model import CohereModel

# Custom CSS for the design system
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
    }
    .subtitle {
        font-size: 1.5em;
        background: linear-gradient(90deg, #FF490E 0%, #FF7B02 100%);
        -webkit-background-clip: text;
        color: transparent;
        text-align: center;
        margin-bottom: 20px;
    }
    .container {
        padding: 20px;
        border-radius: 10px;
        background-color: #FF7B02;
    }
    .stButton>button {
        background: linear-gradient(90deg, #FF490E 0%, #FF7B02 100%);
        border: none;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the logo with a specific width
st.image("hunza.ai.png", use_column_width=False, width=100)

# st.markdown('<div class="title">Hunza.ai</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Plan your next adventure in seconds with AI</div>', unsafe_allow_html=True)

with st.expander("Instructions"):
    st.write("""
    1. Enter the travel destination.
    2. Provide the number of nights.
    3. Choose accommodation type.
    4. Specify the trip type.
    5. Enter the group size.
    """)

def ask_question(question, key):
    if key not in st.session_state:
        st.session_state[key] = ""
    st.session_state[key] = st.text_input(question, value=st.session_state[key])
    if st.button('Next'):
        st.session_state.page += 1
        st.experimental_rerun()

if 'responses' not in st.session_state:
    st.session_state['responses'] = {}
if 'page' not in st.session_state:
    st.session_state['page'] = 0

cohere_model = CohereModel()

questions = [
    ("Where do you want to travel in Pakistan (can be multiple locations)?", 'locations'),
    ("How many nights will you be traveling for?", 'nights'),
    ("Do you want high-end or economy accommodations?", 'accommodations'),
    ("Do you want the trip to be adventure-centric or laid-back?", 'type'),
    ("How many people are in your group?", 'group_size')
]

with st.container():
    if st.session_state.page < len(questions):
        ask_question(*questions[st.session_state.page])
    else:
        st.write("Thank you for providing the details. Generating your itinerary...")
        responses = {key: st.session_state[key] for _, key in questions}
        prompt = cohere_model.create_prompt(responses)
        itinerary = cohere_model.generate_itinerary(prompt)
        st.write(itinerary)

    if st.session_state.page > 0:
        if st.button('Previous'):
            st.session_state.page -= 1
            st.experimental_rerun()
