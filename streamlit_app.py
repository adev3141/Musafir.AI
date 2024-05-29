import streamlit as st
from cohere_model import CohereModel

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

api_key = 'your-api-key'  # Replace with your actual API key
cohere_model = CohereModel(api_key)

questions = [
    ("Where do you want to travel in Pakistan (can be multiple locations)?", 'locations'),
    ("How many nights will you be traveling for?", 'nights'),
    ("Do you want high-end or economy accommodations?", 'accommodations'),
    ("Do you want the trip to be adventure-centric or laid-back?", 'type'),
    ("How many people are in your group?", 'group_size')
]

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
