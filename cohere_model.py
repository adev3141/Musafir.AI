import cohere
import logging
import os

class CohereModel:
    def __init__(self):
        self.api_key = os.getenv('COHERE_API_KEY')
        if not self.api_key:
            raise ValueError("API key not found. Please set the COHERE_API_KEY environment variable.")
        self.client = cohere.Client(self.api_key)
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("CohereModel initialized.")

    def create_prompt(self, responses):
        logging.debug(f"Creating prompt with responses: {responses}")
        prompt = (
            f"You are a travel agent. Create an itinerary for a trip in Pakistan with the following details:\n"
            f"Locations: {responses['locations']}\n"
            f"Number of nights: {responses['nights']}\n"
            f"Accommodation type: {responses['accommodations']}\n"
            f"Trip type: {responses['type']}\n"
            f"Group size: {responses['group_size']}\n"
            "Provide a detailed plan including activities, accommodation, and transportation."
        )
        logging.debug(f"Prompt created: {prompt}")
        return prompt

    def generate_itinerary(self, prompt):
        logging.debug(f"Generating itinerary with prompt: {prompt}")
        try:
            response = self.client.chat(
                message=prompt,
                model='command-r-plus'
            )
            generated_text = response.text
            logging.info("Itinerary generated successfully.")
            logging.debug(f"Model response: {generated_text}")

            # Check if the generated text is the same as the prompt and use a fallback if necessary
            if generated_text.strip() == prompt.strip():
                generated_text = (
                    "Day 1: Arrival in Hunza, check into high-end accommodation, explore the local market.\n"
                    "Day 2: Visit Baltit Fort and Altit Fort, enjoy adventure activities in Karimabad.\n"
                    "Day 3: Trek to Rakaposhi Base Camp, return to hotel for dinner.\n"
                    "Day 4: Day trip to Attabad Lake for boating and adventure sports.\n"
                    "Day 5: Explore Khunjerab Pass, return to Hunza for overnight stay.\n"
                    "Day 6: Departure from Hunza."
                )
            return generated_text
        except Exception as e:
            logging.error(f"Error generating itinerary: {e}")
            raise
