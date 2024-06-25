import sqlite3
conn = sqlite3.connect('langhelp.db')

# Create a cursor object to interact with the database
cur = conn.cursor()
def user():
    while True:
        name = input("Please enter your name: ")
        email = input("Please enter your email: ")
        
        if "@" in email and (email.endswith(".com") or email.endswith(".edu")):
            return name, email
        
        else:
            print("Invalid email address. Please input a valid email")
            
def insertUser():
    name, email = user()
    #Insert the user info into the user table 
    cur.execute('INSERT INTO users (name, email) VALUES (?,?)', (name, email))
    conn.commit()

def askLanguages():

    cur.execute('SELECT DISTINCT language FROM travel_phrases')
    languages = cur.fetchall()
    language_list = [lang[0] for lang in languages]
    for i, language in enumerate(language_list):
        print(f"{i+1}: {language}")
    try:
        user_language_ind = int(input("\nSelect your language from the list above by entering it's number: "))
    except ValueError:
        print("The input was not a valid integer.") 

    try:
        travel_language_ind = int(input("Select the language of the country you are visiting by entering it's number: "))
    except ValueError:
        print("The input was not a valid integer.")
    
    user_language = language_list[user_language_ind - 1]
    travel_language = language_list[travel_language_ind - 1]





    # Code to select languages
    cur.execute(f'''
        SELECT
            phrase1, phrase2, phrase3, phrase4, phrase5, phrase6, phrase7, phrase8, phrase9, phrase10,
            phrase11, phrase12, phrase13, phrase14, phrase15, phrase16, phrase17, phrase18, phrase19, phrase20,
            phrase21, phrase22, phrase23, phrase24, phrase25
        FROM travel_phrases
        WHERE language = ?
    ''', (user_language,))
    user_phrases = cur.fetchone()

    cur.execute(f'''
        SELECT
            phrase1, phrase2, phrase3, phrase4, phrase5, phrase6, phrase7, phrase8, phrase9, phrase10,
            phrase11, phrase12, phrase13, phrase14, phrase15, phrase16, phrase17, phrase18, phrase19, phrase20,
            phrase21, phrase22, phrase23, phrase24, phrase25
        FROM travel_phrases
        WHERE language = ?
    ''', (visiting_language,))
    visiting_phrases = cur.fetchone()


            
            