import streamlit as st
from cohere_model import CohereModel
from fpdf import FPDF
import datetime

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
        text-align: left;
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
    .stDownloadButton>button {
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
    .itinerary {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        color: #2B2D42;
    }
    .itinerary h3 {
        color: #FA3E01;
    }
    .itinerary h4 {
        color: #1B435A;
    }
    .itinerary p {
        font-style: italic;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the logo with a specific width
st.image("hunza.ai.png", use_column_width=False, width=75)

#st.markdown('<div class="title">Hunza.ai</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Let our powerful AI plan your adventure in seconds</div>', unsafe_allow_html=True)

with st.expander("Instructions"):
    st.write("""
    1. Enter the travel destination.
    2. Provide the starting date.
    3. Provide the number of nights.
    4. Choose accommodation type.
    5. Specify the trip type.
    6. Enter the group size.
    """)

def ask_question(question, key, input_type="text"):
    if key not in st.session_state:
        st.session_state[key] = ""

    if input_type == "date":
        st.session_state[key] = st.date_input(question)
    else:
        st.session_state[key] = st.text_input(question, value=st.session_state[key])

    if st.button('Next'):
        st.session_state.page += 1
        st.experimental_rerun()

if 'responses' not in st.session_state:
    st.session_state['responses'] = {}
if 'page' not in st.session_state:
    st.session_state['page'] = 0
if 'itinerary' not in st.session_state:
    st.session_state['itinerary'] = ""

cohere_model = CohereModel()

questions = [
    ("Where do you want to travel in Pakistan (can be multiple locations)?", 'locations', 'text'),
    ("When will your trip start?", 'start_date', 'date'),
    ("How many nights will you be traveling for?", 'nights', 'text'),
    ("Do you want high-end or economy accommodations?", 'accommodations', 'text'),
    ("Do you want the trip to be adventure-centric or laid-back?", 'type', 'text'),
    ("How many people are in your group?", 'group_size', 'text')
]

def generate_pdf(itinerary_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, itinerary_text)
    return pdf.output(dest='S').encode('latin1')

with st.container():
    if st.session_state.page < len(questions):
        question, key, input_type = questions[st.session_state.page]
        ask_question(question, key, input_type)
    else:
        st.write("Thank you for providing the details. Generating your itinerary...")
        responses = {key: st.session_state[key] for _, key, _ in questions}
        prompt = cohere_model.create_prompt(responses)
        st.session_state['itinerary'] = cohere_model.generate_itinerary(prompt)
        
        # Display the itinerary in a styled format
        st.markdown('<div class="itinerary"><h3>Your Itinerary</h3>' + st.session_state['itinerary'].replace('\n', '<br>') + '</div>', unsafe_allow_html=True)
        
        # Generate and provide a download link for the PDF only if the itinerary is generated
        if st.session_state['itinerary']:
            pdf_content = generate_pdf(st.session_state['itinerary'])
            st.download_button(
                label="Download Itinerary as PDF",
                data=pdf_content,
                file_name=f"itinerary_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                mime="application/octet-stream"
            )

    if st.session_state.page > 0:
        if st.button('Previous'):
            st.session_state.page -= 1
            st.experimental_rerun()