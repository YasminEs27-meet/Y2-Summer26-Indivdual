import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = " You are a Coding Debugger and your name is yossi jonior. Help users find and fix bugs, explain errors clearly, provide corrected code, ask for missing information when needed, and keep explanations simple. Never invent errors, change the code's purpose, provide unsafe code, or criticize the user"
    

    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})
        print('History:', history)
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )
        print (response)
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



#second lab
#Input tokens are the text, system prompts, and files you send into theAI, while output tokens are the text the model generates in response

#Step 2: Experiment — Change the parameters

# If we change `max_tokens` to **50** and ask a long question, Claude will return a much shorter response because the output is limited to **50 tokens**, so the answer may be cut off or incomplete.
#With temperature = 0, the AI will usually give the same or nearly identical answer each time you send the same message because randomness is minimized.
#With temperature = 1, the AI's answers become more varied and creative, so the same message may produce different responses each time
#Temperature controls the randomness and creativity of the AI's responses—lower values make answers more consistent, while higher values make them more varied and creative.

#Step 3: Read the history — See the messages list
#They don't save your chat history on their end to keep things fast and secure. So, if you don't send the whole chat history every time,the API completely forgets what you were talking about two seconds ago

# Reflection — Lab 0.2
#you are staing at a hotle and each time you open the fridge and take somthing the cost wil rase immedtiatly and evry time you take somthing out the cost will rise and you have to pay them later 
#thought the code would run fine and print Claude's response, maybe
#just duplicating it since there are two print statements back-to-back
#The code crashes with a NameError: name 'reply' is not defined
#reliazed that python reads code line-by-line from top to bottom

#lab 3

#Step 3: Test — Validate behavior across multiple turns
# if i ask him about other things he will tell me that he is a coding debugger and will not answer my questions about other things

#reflection — Lab 0.3
#I think when you use any app in your phone, like snapchat, instagram, or tiktok, you see only the output and not the underlying process
# the AI will lose its foundational instructions. It will revert to a generic, unconstrained chatbot, often defaulting to a standard, unguided conversational tone and ignoring specific rules or personas
#A single high-impact "Always / Never" rule forces the AI to break default conversational habits. 
#transforming conversational replies into scannable, markdown-formatted layouts

#3- i  had a conection issue and it was not working for a while but then i fixed it and it worked fine  





