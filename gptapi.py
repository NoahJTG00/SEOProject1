import os 
import openai
from dotenv import load_dotenv
from openai import OpenAI



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
def chat():
    
    while True:
        user_input = input("You:")
        
        if user_input.lower() in ['exit', 'quit']:
            print('Thank you!')
            break
            
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a a user in need of linguistic help"},
                {"role": "user", "content": user_input}
            ]
        )
        print(completion.choices[0].message.content)
        
chat()



