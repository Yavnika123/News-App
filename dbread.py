import sqlite3

# Connect to the SQLite database file
connection = sqlite3.connect('db.sqlite3')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Get the table names from the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = cursor.fetchall()

# Iterate over the table names and print the data
for table_name in table_names:
    print(f"Table: {table_name[0]}")
    cursor.execute(f"SELECT * FROM {table_name[0]};")
    table_data = cursor.fetchall()
    for row in table_data:
        print(row)

# Close the cursor and the database connection
cursor.close()
connection.close()