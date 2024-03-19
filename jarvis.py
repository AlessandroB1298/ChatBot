import os
import time
from gtts import gTTS
import openai

API_KEY = "***********************************"
openai.api_key= API_KEY

def send_message(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    print(response.choices[0].message.content)

# Main loop for the chat
while True:
    user_input = input("You: ")  # Get user input
    send_message(user_input) 