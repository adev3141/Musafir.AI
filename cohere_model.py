import logging
import os
import cohere


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
            f"You are an experienced travel agent specializing in creating detailed itineraries for trips in Pakistan. Your task is to create a realistic and well-organized itinerary, considering travel times, most used routes to reach destinations, local events, and national holidays. Use the following details to craft the itinerary:\n"
            f"- Locations: {responses['locations']}\n"
            f"- Starting Date: {responses['start_date']}\n"
            f"- Number of Nights: {responses['nights']}\n"
            f"- Accommodation Type: {responses['accommodations']}\n"
            f"- Trip Type (Adventure or Laid-back): {responses['type']}\n"
            f"- Group Size: {responses['group_size']}\n\n"
            "Ensure the itinerary meets the following requirements:\n"
            "- Use major highways and most feasible routes for travel between destinations\n"
            "- Calculate realistic travel times, avoiding impractical routes (e.g., mountain roads unless necessary)\n"
            "- Provide detailed daily activities and sightseeing spots\n"
            "- Include accommodation details for each night\n"
            "- Highlight events or festivals happening during the trip dates and their impact on travel plans\n"
            "- Include transportation details between locations, specifying travel times and routes\n"
            "- Recommend local cuisine and dining options at each stop\n"
            "- Consider road conditions and possible delays to ensure a smooth travel experience"
        )

        logging.debug(f"Prompt created: {prompt}")
        return prompt

    def generate_itinerary(self, prompt):
        logging.debug(f"Our AI is going its magic: {prompt}")
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
                    "Oooops! Looks like we've reached our daily limit of giving out free itineraries."
                )
            return generated_text
        except Exception as e:
            logging.error(f"Error generating itinerary: {e}")
            raise
