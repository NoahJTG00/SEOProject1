import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('langhelp.db')

# Create a cursor object to interact with the database
cur = conn.cursor()

# Created a user table
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT,
        CHECK (email LIKE '%_@_%._%' AND (email LIKE '%.com' OR email LIKE '.edu'))
    )
''')
#Create a language table

cur.execute('''
            CREATE TABLE IF NOT EXISTS language (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                language TEXT NOT NULL, 
                translation TEXT,
                phrase TEXT
    
)''')
          

# Insert data into the table
cur.execute('''
    INSERT INTO users (name, email) VALUES
    ('Alice', 'alice12@gmail.com'),
    ('Bob', 'bob@gmail.com')
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

