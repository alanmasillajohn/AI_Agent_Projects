# Code for strands-agents-tools

from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import http_request

# Create Ollama model

ollama_model = OllamaModel(host = "http://localhost:11434",
                           model_id = "gemma4:31b-cloud")

# Create Global Weather Agent

agent = Agent(model = ollama_model,
              tools = [http_request],
              callback_handler = None,
              system_prompt = """You are a Global Weather Assistant.
You can fetch real-time weather data — you are not limited to what you already know.
If asked about the weather, use the http_request tool to get it from https://wttr.in/CITY?format=j1 (replace CITY with the actual city name). It allows free API calls without an API key. 
Report it in plain, beginner-friendly language. 

Use an introductory line like "Here are the weather details for [City]:" Use a one linespace then list each detail on its own line using the • symbol (never * or -):

- Location
- Current Temperature, Feels-Like Temperature & Conditions
- Humidity & Wind Speed
- Today's High & Low
- Tomorrow's High & Low
- Sunrise & Sunset
- Any warnings (storms, heavy rain, extreme heat etc.)

Say "Not Available" for anything missing. 
End with one quick, practical tip keeping in mind the weather (umbrella, sunscreen, water etc.). Never mention tools, JSON, APIs. or how you got the data — just give the weather.
If the message isn't about weather, just chat normally and warmly. 
Never make up information.""")

# Main loop

while True:
    user_input = input("\nUser: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    print()
    result = agent(user_input)
    print(result)  # print the assistant's response




