import logging
from transformers import pipeline

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Explicitly set the device to CPU
device = "cpu"

# Log the device being used
logging.info(f"Setting device to {device}")

try:
    # Load the model
    model_id = "THUDM/agentlm-7b"  # Replace with the appropriate model ID
    logging.info(f"Loading model with ID: {model_id}")
    generator = pipeline("text-generation", model=model_id, device=device)
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    raise

def generate_itinerary(prompt):
    logging.debug(f"Generating itinerary with prompt: {prompt}")
    try:
        response = generator(prompt, max_length=500, truncation=True)
        logging.info("Itinerary generated successfully.")
        logging.debug(f"Model response: {response}")
        return response[0]['generated_text']
    except Exception as e:
        logging.error(f"Error generating itinerary: {e}")
        raise

def create_prompt(responses):
    logging.debug(f"Creating prompt with responses: {responses}")
    prompt = (
        f"You are a experienced travel agent in Pakistan specializing in itinerary creation. Create a realistic itinerary with correct travel times for a trip in Pakistan. Check for any national holidays or festivals happening in the area selected and inform that in the itinerary the effect of those events with the following details:\n"
        f"Locations: {responses['locations']}\n"
        f"Locations: {responses['date']}\n"
        f"Number of nights: {responses['nights']}\n"
        f"Accommodation type: {responses['accommodations']}\n"
        f"Trip type: {responses['type']}\n"
        f"Group size: {responses['group_size']}\n"
        "Provide a detailed plan including activities, accommodation, events happening during those dates and transportation."
    )
    logging.debug(f"Prompt created: {prompt}")
    return prompt
