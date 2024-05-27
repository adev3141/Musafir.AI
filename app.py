# app.py

import logging
import streamlit as st
from model import create_prompt, generate_itinerary

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize session state
if 'responses' not in st.session_state:
    st.session_state['responses'] = {}
    st.session_state['page'] = 0
    logging.info("Session state initialized.")

def ask_question(question, key):
    st.session_state['responses'][key] = st.text_input(question)
    if st.button('Next'):
        st.session_state['page'] += 1
        logging.debug("Next button clicked. Current page: %s", st.session_state['page'])

# Define questions
questions = [
    ("Where do you want to travel in Pakistan (can be multiple locations)?", 'locations'),
    ("How many nights will you be traveling for?", 'nights'),
    ("Do you want high-end or economy accommodations?", 'accommodations'),
    ("Do you want the trip to be adventure-centric or laid-back?", 'type'),
    ("How many people are in your group?", 'group_size')
]

# Show questions
if st.session_state['page'] < len(questions):
    ask_question(*questions[st.session_state['page']])
else:
    st.write("Thank you for providing the details. Generating your itinerary...")
    responses = st.session_state['responses']
    logging.debug("Responses collected: %s", responses)
    prompt = create_prompt(responses)
    logging.debug("Generated prompt: %s", prompt)
    try:
        itinerary = generate_itinerary(prompt)
        st.write(itinerary)
        logging.info("Itinerary displayed successfully.")
    except Exception as e:
        st.write("An error occurred while generating the itinerary. Please try again.")
        logging.error("Error generating itinerary: %s", e)

if st.session_state['page'] > 0:
    if st.button('Previous'):
        st.session_state['page'] -= 1
        logging.debug("Previous button clicked. Current page: %s", st.session_state['page'])
