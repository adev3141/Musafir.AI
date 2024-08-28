import streamlit as st
from gemini_model import GeminiModel
from fpdf import FPDF
import datetime

# Custom CSS for the design system, blinking effect, and to increase the size of the displayed questions
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
    .stButton>button, .stDownloadButton>button {
        background: linear-gradient(90deg, #FF490E 0%, #FF7B02 100%);
        border: none;
        color: white;
        padding: 10px 20px;
        text-align: center;
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
    .question {
        font-size: 1.3em;  /* Increased font size */
        color: #FA3E01;
    }
    .question-input {
        font-size: 0.9em;
        padding: 10px;
    }
    .input-blink {
        animation: blink 1s step-end 3;
    }
    @keyframes blink {
        50% {
            border-color: #FF0000;
        }
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
    </style>
    """,
    unsafe_allow_html=True
)

# Display the logo with a specific width
st.image("logo/hunza.ai.png", use_column_width=False, width=75)

# Title and Subtitle
st.markdown('<div class="subtitle">Let 3M AI plan your adventure in seconds</div>', unsafe_allow_html=True)

# Instructions
with st.expander("Instructions"):
    st.write("""
    1. Enter the travel destination.
    2. Provide the starting location.
    3. Provide the starting date.
    4. Provide the number of nights.
    5. Choose accommodation type.
    6. Specify the trip type.
    7. Enter the group size.
    """)

# Initialize session state variables
if 'responses' not in st.session_state:
    st.session_state['responses'] = {}
if 'page' not in st.session_state:
    st.session_state['page'] = 0  # Ensure 'page' is initialized correctly
if 'itinerary' not in st.session_state:
    st.session_state['itinerary'] = ""
if 'invalid_msg' not in st.session_state:
    st.session_state['invalid_msg'] = ""

gemini_model = GeminiModel()

# Define the questions and their properties
questions = [
    ("Where do you want to travel in Pakistan (can be multiple locations)?", 'locations', 'text'),
    ("What's your starting location?", 'starting_location', 'text'),
    ("When will your trip start?", 'start_date', 'date'),
    ("How many nights will you be traveling for?", 'nights', 'text'),
    ("Do you want high-end or economy accommodations?", 'accommodations', 'text'),
    ("Do you want the trip to be adventure-centric or laid-back?", 'type', 'text'),
    ("How many people are in your group?", 'group_size', 'text')
]

def generate_pdf(itinerary_text, logo_path):
    # Replace unsupported characters with alternatives
    itinerary_text = itinerary_text.replace('\u2013', '-').replace('\u2014', '--')

    subtitle = "\n\nNote: This itinerary is AI-generated and may be subject to change."
    complete_text = itinerary_text + subtitle
    
    class PDF(FPDF):
        def header(self):
            self.image(logo_path, 10, 8, 33)  # Adjust the position and size as needed
            self.set_font("Arial", 'B', 12)
            self.cell(0, 10, 'Itinerary', ln=True, align='C')
            self.ln(20)
    
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, complete_text.encode('latin-1', 'replace').decode('latin-1'))
    
    return pdf.output(dest='S').encode('latin-1')

def format_itinerary(itinerary):
    # Splitting the generated itinerary by lines and reformatting it as HTML
    days = itinerary.split('##')
    formatted_itinerary = ""
    for day in days:
        if day.strip():
            formatted_itinerary += f"<div class='itinerary'>{day.strip()}</div>"
    formatted_itinerary += "<div class='itinerary'><p><em>Note: This itinerary is AI-generated and may be subject to change.</em></p></div>"
    return formatted_itinerary

# Main container for the questionnaire and logic
with st.container():
    if st.session_state.page < len(questions):
        question, key, input_type = questions[st.session_state.page]

        with st.form(key=f'form_{st.session_state.page}'):
            st.markdown(f'<div class="question">{question}</div>', unsafe_allow_html=True)

            if input_type == "date":
                response = st.date_input("", key=key, label_visibility="collapsed")
            else:
                response = st.text_input("", key=key, label_visibility="collapsed")

            error_message = st.session_state.get('invalid_msg', "")
            if error_message:
                st.markdown(f'<div style="color: red; font-weight: bold;">{error_message}</div>', unsafe_allow_html=True)

            next_clicked = st.form_submit_button('Next')
            
            if next_clicked:
                if response:
                    st.session_state.responses[key] = response
                    st.session_state.page += 1  # Properly increment the page number
                    st.session_state['invalid_msg'] = ""  # Clear the error message
                    st.rerun()  # Rerun the script to update the page
                else:
                    st.session_state['invalid_msg'] = "This field is required! Please enter a valid response."
                    st.rerun()  # Rerun the script to update the page

    else:
        st.write("Thank you for providing the details. I am now creating the best, most realistic itinerary for you...")
        responses = st.session_state.responses
        prompt = gemini_model.create_prompt(responses)
        st.session_state.itinerary = gemini_model.generate_itinerary(prompt)

        # Format and display the itinerary
        if st.session_state.itinerary:
            formatted_itinerary = format_itinerary(st.session_state.itinerary)
            st.markdown(f'<div class="itinerary"><h4>Itinerary for {responses["locations"]}, {int(responses["nights"])+1} days</h4>{formatted_itinerary}</div>', unsafe_allow_html=True)

            # Generate and provide a download link for the PDF
            logo_path = "logo/logo.png"  
            pdf_content = generate_pdf(st.session_state.itinerary, logo_path)
            st.download_button(
                label="Download Itinerary as PDF",
                data=pdf_content,
                file_name=f"itinerary_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                mime="application/pdf"
            )
        else:
            st.error("There was an issue generating the itinerary. Please try again.")

    # Display Previous button only if not on the first page and no itinerary is displayed
    if st.session_state.page > 0 and st.session_state.page < len(questions):
        if st.button('Previous'):
            st.session_state.page -= 1
            st.session_state['invalid_msg'] = ""  # Clear any error messages when going back
            st.rerun()  # Rerun the script to update the page

# Footer
st.markdown('<div class="footer">All rights reserved | Created by ADev</div>', unsafe_allow_html=True)
