import os 
import sqlite3
import openai
from tabulate import tabulate
from gptapi import *
from openai import OpenAI

conn = sqlite3.connect('langhelp.db')

# Create a cursor object to interact with the database
cur = conn.cursor()
def user():
    while True:
        name = input("Username: ")
        password = input("Password: ")
        
        return name, password
        
            
def insertUser():
    while True:
        name, password = user()
        
        # Check if the user already exists
        cur.execute('''
            SELECT 1 FROM users WHERE name = ? AND password = ?
        ''', (name, password))
        
        if cur.fetchone() is None:
            try:
                cur.execute('INSERT INTO users (name, password) VALUES (?, ?)', (name, password))
                conn.commit()
                return name, password  # Exit the loop after successful insertion
            except sqlite3.IntegrityError:
                print(f"Username '{name}' already exists. Please select another one.")
        else:
            return name, password


def askLanguages(username, password):
    cur.execute('''
        SELECT native_language FROM users 
        WHERE name = ? AND password = ?
    ''', (username, password))
    
    result = cur.fetchone()
    if not result[0]:

        cur.execute('SELECT DISTINCT language FROM language')
        languages = cur.fetchall()
        language_list = [lang[0] for lang in languages]
        cur.execute('SELECT statement FROM language')
        statements = cur.fetchall()

        # Separate the statements into a list
        statement_list = [statement[0] for statement in statements]
        print("")
        while True:
            for statement in statement_list:
                print(statement)
            try:
                user_language_ind = int(input("\n"))
            except ValueError:
                print("The input was not a valid integer.\n")
            if user_language_ind > 10 or user_language_ind < 1:
                print("Please enter a number between 1 and 10.\n")
                continue
            else:
                break
        
        user_language = language_list[user_language_ind - 1]
        cur.execute('''
        UPDATE users 
        SET native_language = ? 
        WHERE name = ? AND password = ?
        ''', (user_language, username, password))
        conn.commit()

    else:
        user_language = result[0]
    
    query = f'SELECT {user_language} FROM languages_translation'
    cur.execute(query)

    # Fetch all results
    user_languages = cur.fetchall()

    # Print the results
    

    while True:
        print("")
        for i, language in enumerate(user_languages, start=1):
            print(f"{i}. {language[0]}")
        print("\n")    
        try:
            travel_language_ind = int(print_translate("Select the language of the country you are visiting by entering it's number", user_language, ": ", True))
        except ValueError:
            print_translate("The input was not a valid integer", user_language, ".")
        if travel_language_ind > 10 or travel_language_ind < 1:
            print_translate("Please enter a number between 1 and 10", user_language, en=".\n")
            continue
        else:
            break

    
    visiting_language = language_list[travel_language_ind - 1]

    # Code to select languages
    cur.execute(f'''
        SELECT
            phrase1, phrase2, phrase3, phrase4, phrase5, phrase6, phrase7, phrase8, phrase9, phrase10,
            phrase11, phrase12, phrase13, phrase14, phrase15, phrase16, phrase17, phrase18, phrase19, phrase20,
            phrase21, phrase22, phrase23, phrase24, phrase25
        FROM language
        WHERE language = ?
    ''', (user_language,))
    user_phrases = cur.fetchone()

    cur.execute(f'''
        SELECT
            phrase1, phrase2, phrase3, phrase4, phrase5, phrase6, phrase7, phrase8, phrase9, phrase10,
            phrase11, phrase12, phrase13, phrase14, phrase15, phrase16, phrase17, phrase18, phrase19, phrase20,
            phrase21, phrase22, phrase23, phrase24, phrase25
        FROM language
        WHERE language = ?
    ''', (visiting_language,))
    visiting_phrases = cur.fetchone()
    return user_phrases, visiting_phrases, user_language, visiting_language

def printTable(user_phrases, visiting_phrases, user_language, visiting_language):

    table_data = []
    for i in range(25):
        table_data.append([f"Phrase {i + 1}", user_phrases[i], visiting_phrases[i]])

    # Print the phrases in a nice table format
    print()
    print_translate("Common Travel Phrases", user_language, ": \n")
    print(tabulate(table_data, headers=["Phrase #", user_language, visiting_language], tablefmt="grid"))
    
    
    
    

def practice_phrases(user_phrases, visiting_phrases, user_language, visiting_language):
    while True:
        printTable(user_phrases, visiting_phrases, user_language, visiting_language)
        try:
            print()
            num_phrase = int(print_translate("Enter the phrase number you want to practice (1 - 25) or 0 to exit", user_language, ": ", True))

            if num_phrase == 0:
                print_translate("Thank you", user_language, "!")
                break
            
            if num_phrase < 1 or num_phrase > 25:
                print_translate("Please enter a number between 1 and 25", user_language, ".\n")
                continue
            
            practice = visiting_phrases[num_phrase -1]
            print_translate("Practice Phrase ", user_language, " ")
            print(f"{num_phrase} : {practice}\n\n")
            
            res = chat(practice, user_language, visiting_language)
            if res == 0:
                break
            
        
        except ValueError:
            print("The input was not a valid integer")

def main():
    insertUser()
    user_phrases, visiting_phrases, user_language, visiting_language = askLanguages()
    practice_phrases(user_phrases, visiting_phrases, user_language, visiting_language)

if __name__ == "__main__":
    main()
            


            
            


            
            