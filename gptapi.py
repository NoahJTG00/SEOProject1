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

# Translate any phrase
def print_translate(phrase, user_language, en, inpt=False):
    translated_phrase = phrase
    if user_language != 'English':
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant proficient in {user_language} and English. Please base your response only on the provided phrase and return it with no punctuation at the end."},
            {"role": "user", "content": f"Please translate the following phrase from English to {user_language}: {phrase}"}
        ]
        )
        translated_phrase = completion.choices[0].message.content
    if inpt:
        return input(translated_phrase + en)
    else:
        print(translated_phrase + en, end = "")

# Specify the model to use and the messages to send
def chat(practice, user_language, visiting_language):

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant proficient in {user_language} and {visiting_language}. Please respond as if the user only spoke {user_language}, but provide examples in {visiting_language} so they can learn how to use them."},
            {"role": "user", "content": f"Please conjugate the following phrase in {visiting_language} and provide examples of its usage: '{practice}'"}
        ]
    )
    print(completion.choices[0].message.content)
    
    while True:
        print("\n")
        user_input = print_translate("Do you have any questions about the above phrase? (Enter 0 to quit or -1 to select another phrase)", user_language, "\n", True)
        
        if user_input == '-1':
            return 1

        if user_input == '0':
            print_translate('Thank you', user_language, "!")
            return 0
        
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant proficient in {user_language} and {visiting_language}. Please respond as if the user only spoke {user_language} and was trying to learn {visiting_language}"},
                {"role": "user", "content": f"{user_input}"}
            ]
        )
        print(f"\n\n{completion.choices[0].message.content}")
    