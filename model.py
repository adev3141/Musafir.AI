# model.py

import logging
from transformers import pipeline

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Initializing model...")

try:
    # Load the model
    model_id = "THUDM/agentlm-7b"  # Replace with the appropriate model ID
    generator = pipeline("text-generation", model=model_id, device=device)
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error("Error loading model: %s", e)
    raise

def generate_itinerary(prompt):
    logging.debug("Generating itinerary with prompt: %s", prompt)
    try:
        response = generator(prompt, max_length=500)
        logging.info("Itinerary generated successfully.")
        return response[0]['generated_text']
    except Exception as e:
        logging.error("Error generating itinerary: %s", e)
        raise

def create_prompt(responses):
    logging.debug("Creating prompt with responses: %s", responses)
    prompt = (
        f"You are a travel agent. Create an itinerary for a trip in Pakistan with the following details:\n"
        f"Locations: {responses['locations']}\n"
        f"Number of nights: {responses['nights']}\n"
        f"Accommodation type: {responses['accommodations']}\n"
        f"Trip type: {responses['type']}\n"
        f"Group size: {responses['group_size']}\n"
        "Provide a detailed plan including activities, accommodation, and transportation."
    )
    logging.debug("Prompt created: %s", prompt)
    return prompt
