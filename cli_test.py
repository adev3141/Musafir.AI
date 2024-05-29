import logging
from model import create_prompt, generate_itinerary

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    responses = {}

    # Collect user input via CLI
    responses['locations'] = input("Where do you want to travel in Pakistan (can be multiple locations)? ")
    responses['nights'] = input("How many nights will you be traveling for? ")
    responses['accommodations'] = input("Do you want high-end or economy accommodations? ")
    responses['type'] = input("Do you want the trip to be adventure-centric or laid-back? ")
    responses['group_size'] = input("How many people are in your group? ")

    logging.debug(f"Responses collected: {responses}")

    # Create the prompt
    prompt = create_prompt(responses)
    logging.debug(f"Generated prompt: {prompt}")

    # Generate the itinerary
    try:
        itinerary = generate_itinerary(prompt)
        print("Generated Itinerary:")
        print(itinerary)
        logging.info("Itinerary displayed successfully.")
    except Exception as e:
        print("An error occurred while generating the itinerary. Please try again.")
        logging.error(f"Error generating itinerary: {e}")

if __name__ == "__main__":
    main()
