import sqlite3

# make a connection to the database
conn = sqlite3.connect('sqlite3/customer.db')

# Create a cursor
c = conn.cursor()

# Query the database - with a LIMIT at the END
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")

items = c.fetchall()

for item in items:
    print(item)

# close our connection
conn.close()
