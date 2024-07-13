Travel Itinerary Generator

This project is a travel itinerary generator specifically designed for creating detailed travel plans for trips in Pakistan. The generator uses Cohere's AI model to craft itineraries based on user input, considering travel times, routes, local events, national holidays, and other essential factors.

Features

Create realistic and well-organized itineraries.
Calculate travel times and suggest feasible routes.
Provide detailed daily activities and sightseeing spots.
Include accommodation details for each night.
Highlight local events and festivals.
Recommend local cuisine and dining options.
Consider road conditions and possible delays.

Installation

1. Clone the repository:

git clone https://github.com/yourusername/travel-itinerary-generator.git
cd travel-itinerary-generator

2. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required dependencies:

pip install -r requirements.txt

4. Set up your Cohere API key:

export COHERE_API_KEY='your_cohere_api_key'  # On Windows, use `set COHERE_API_KEY=your_cohere_api_key`

Usage

1. Run the Streamlit app:

streamlit run streamlit_app.py

2. Open your browser and go to http://localhost:8501 to use the travel itinerary generator.

File Structure

streamlit_app.py: Contains the Streamlit app code for the user interface.
cohere_model.py: Contains the code for interacting with the Cohere AI model to generate itineraries.

