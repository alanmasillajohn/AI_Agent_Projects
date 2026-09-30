# Code for strands-agents

from strands import Agent
from strands.models.ollama import OllamaModel

# Create an Ollama model instance

ollama_model = OllamaModel(host = "http://localhost:11434",  # Ollama server address
                           model_id = "llama3.1:8b")   # Specify which model to use

# Create an agent using the Ollama model

agent = Agent(model = ollama_model,
              system_prompt = "You are an helpful assistant who chats in a friendly way with the user.")

# Use the agent

while True:
    user_input = input("\nUser: ")
    print()
    
    agent(user_input)
    print()
    