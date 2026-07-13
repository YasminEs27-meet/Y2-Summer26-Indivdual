import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is Alex. You are a helpful but an angry chatbot."
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()
#it's like a group project where someone joins late. If they only hear the last sentence, they'll be confused. They need the whole conversation to understand what's happening
#history.append({'role': 'assistant', 'content': reply}): It saves the assistant's replies so the AI remembers what it said earlier.
#load_dotenv(): It loads the API key from the .env file so the program can connect to the API.
#temperature=0.7: It makes the AI's responses more creative and varied.
#break inside if user_input.lower() == 'exit':: It stops the loop and closes the chat when the user types exit.

#At first it kept showing me erors then i figured it out with nada and hadi that the cloud modle was wrong