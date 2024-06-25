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
            

name, email = user()

#Insert the user info into the user table 
cur.execute('INSERT INTO users (name, email) VALUES (?,?)', (name, email))
conn.commit()


            
            