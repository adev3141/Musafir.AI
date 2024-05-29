import streamlit as st
from cohere_model import CohereModel

def ask_question(question, key):
    st.session_state['responses'][key] = st.text_input(question)
    if st.button('Next'):
        st.session_state['page'] += 1

if 'responses' not in st.session_state:
    st.session_state['responses'] = {}
    st.session_state['page'] = 0

api_key = 'tkhCHTdt5MtuFdc7uB7o1XrhHJFFrY6nt63DpsC6'  # Replace with your actual API key
cohere_model = CohereModel(api_key)

questions = [
    ("Where do you want to travel in Pakistan (can be multiple locations)?", 'locations'),
    ("How many nights will you be traveling for?", 'nights'),
    ("Do you want high-end or economy accommodations?", 'accommodations'),
    ("Do you want the trip to be adventure-centric or laid-back?", 'type'),
    ("How many people are in your group?", 'group_size')
]

if st.session_state['page'] < len(questions):
    ask_question(*questions[st.session_state['page']])
else:
    responses = st.session_state['responses']
    prompt = cohere_model.create_prompt(responses)
    itinerary = cohere_model.generate_itinerary(prompt)
    st.write(itinerary)

if st.session_state['page'] > 0:
    if st.button('Previous'):
        st.session_state['page'] -= 1
