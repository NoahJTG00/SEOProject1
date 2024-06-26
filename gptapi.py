import os 
import openai
from dotenv import load_dotenv
from openai import OpenAI
from insertData import *


# Load environment variables from a .env file
load_dotenv()

# Set environment variables
my_api_key = os.getenv("OPENAI_KEY")

openai.api_key = my_api_key
# WRITE YOUR CODE HERE

client = OpenAI(
    api_key=my_api_key,
)

# Specify the model to use and the messages to send
def chat(practice, user_language, visiting_language):
    
    while True:
        user_input = input("You:")
        
        if user_input.lower() in ['exit', 'quit']:
            print('Thank you!')
            break
            
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant proficient in {user_language} and {visiting_language}. Please base your response only on the provided phrase."},
                {"role": "user", "content": f"Please conjugate the following phrase in {visiting_language} and provide examples of its usage: '{practice}'"}
            ]
        )
        print(completion.choices[0].message.content)
        



