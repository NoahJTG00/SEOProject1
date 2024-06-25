import sqlite3

conn = sqlite3.connect('langhelp.db')
cur = conn.cursor()

cur.execute("SELECT email FROM users;")

# Fetch all results
tables = cur.fetchall()

# Print table names
print("Records in the database:")
for table in tables:
    print(table[0])

# Close the connection
conn.close()
