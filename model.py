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
        f"You are an experienced travel agent specializing in creating detailed itineraries for trips in Pakistan. Your task is to create a realistic and well-organized itinerary, considering travel times, local events, and national holidays. Use the following details to craft the itinerary:\n"
        f"- Locations: {responses['locations']}\n"
        f"- Starting Date: {responses['start_date']}\n"
        f"- Number of Nights: {responses['nights']}\n"
        f"- Accommodation Type: {responses['accommodations']}\n"
        f"- Trip Type (Adventure or Laid-back): {responses['type']}\n"
        f"- Group Size: {responses['group_size']}\n\n"
        "Provide a comprehensive plan that includes:\n"
        "- Daily activities and sightseeing spots\n"
        "- Accommodation details for each night\n"
        "- Events or festivals happening during the trip dates and their impact on travel plans\n"
        "- Transportation details between locations, including travel times\n"
        "- Recommendations for local cuisine and dining options"
    )
    logging.debug(f"Prompt created: {prompt}")
    return prompt
