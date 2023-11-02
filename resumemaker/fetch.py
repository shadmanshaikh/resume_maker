import sqlite3

# Open a connection to the SQLite database
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Get a list of all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print the list of tables
print("Tables in the database:")
for table in tables:
    print(table[0])

# Close the cursor and the database connection
cursor.close()
conn.close()
