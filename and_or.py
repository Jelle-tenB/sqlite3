import sqlite3

# make a connection to the database
conn = sqlite3.connect('sqlite3/customer.db')

# Create a cursor
c = conn.cursor()

# Query the database - AND/OR
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' AND rowid = 3")

c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 3")

items = c.fetchall()

for item in items:
    print(item)

# close our connection
conn.close()
