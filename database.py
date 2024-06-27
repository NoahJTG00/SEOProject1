import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('langhelp.db')

# Create a cursor object to interact with the database
cur = conn.cursor()

# Code to DELETE ALL ENTRIES! uncomment as needed
# cur.execute('DROP TABLE IF EXISTS language')
# cur.execute('DROP TABLE IF EXISTS users')
# cur.execute('DROP TABLE IF EXISTS languages_translation')

# cur.execute('DELETE FROM language')
# cur.execute('DELETE FROM users')
# conn.commit()
# conn.close()


def createTables():
    # Created a user table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        password TEXT,
        native_language TEXT
    )
    ''')
    
    #Create a language table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS languages_translation (
        Español TEXT,
        Français TEXT,
        Deutsch TEXT,
        Italiano TEXT,
        Português TEXT,
        Nederlands TEXT,
        Svenska TEXT,
        Norsk TEXT,
        Dansk TEXT,
        English TEXT
        )
    ''')


    # Create the table with columns for each common travel phrase
    cur.execute('''
    CREATE TABLE IF NOT EXISTS language (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        language TEXT NOT NULL,
        statement TEXT,
        phrase1 TEXT,
        phrase2 TEXT,
        phrase3 TEXT,
        phrase4 TEXT,
        phrase5 TEXT,
        phrase6 TEXT,
        phrase7 TEXT,
        phrase8 TEXT,
        phrase9 TEXT,
        phrase10 TEXT,
        phrase11 TEXT,
        phrase12 TEXT,
        phrase13 TEXT,
        phrase14 TEXT,
        phrase15 TEXT,
        phrase16 TEXT,
        phrase17 TEXT,
        phrase18 TEXT,
        phrase19 TEXT,
        phrase20 TEXT,
        phrase21 TEXT,
        phrase22 TEXT,
        phrase23 TEXT,
        phrase24 TEXT,
        phrase25 TEXT
    )
    ''')

    # Commit the changes
    conn.commit()

          



