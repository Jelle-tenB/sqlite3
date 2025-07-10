import sqlite3

# make a connection to the database
conn = sqlite3.connect('sqlite3/customer.db')

# Create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)

# commit changes
conn.commit()

# close our connection
conn.close()
