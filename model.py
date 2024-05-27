# model.py

from transformers import pipeline
import torch

# Explicitly set the device to CPU
device = "cpu"

# Load the model
model_id = "THUDM/agentlm-7b"  # Replace with the appropriate model ID
generator = pipeline("text-generation", model=model_id, device=device)

def generate_itinerary(prompt):
    response = generator(prompt, max_length=500)
    return response[0]['generated_text']

def create_prompt(responses):
    prompt = (
        f"You are a travel agent. Create an itinerary for a trip in Pakistan with the following details:\n"
        f"Locations: {responses['locations']}\n"
        f"Number of nights: {responses['nights']}\n"
        f"Accommodation type: {responses['accommodations']}\n"
        f"Trip type: {responses['type']}\n"
        f"Group size: {responses['group_size']}\n"
        "Provide a detailed plan including activities, accommodation, and transportation."
    )
    return prompt
