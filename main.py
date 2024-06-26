# Main file where everything is ran from
import os
import openai
import sqlite3
import unittest
from dotenv import load_dotenv
from user import *
from insertData import *
from database import *
from openai import OpenAI

'''def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMainFunction)
    
    unittest.TextTestRunner(verbosity = 2).run(suite)'''
    
conn = sqlite3.connect('langhelp.db')

# Create a cursor object to interact with the database
cur = conn.cursor()

# Create table for users and languages
# createTables()

# # # Insert language data
# insertData()

# Query to get all unique languages
cur.execute('SELECT DISTINCT language FROM language')

# Fetch all unique languages
languages = cur.fetchall()

# Print the list of languages
# for language in languages:
#     print(language[0])


# Get information from user and insert into table
#insertUser()
user_phrases, visiting_phrases, user_language, visiting_language = askLanguages()

practice_phrases(user_phrases, visiting_phrases, user_language, visiting_language)


# Commit the changes and close the connection
conn.close()

