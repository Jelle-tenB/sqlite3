import sqlite3

# make a connection to the database
conn = sqlite3.connect('sqlite3/customer.db')

# Create a cursor
c = conn.cursor()

# DELETING
c.execute("DELETE from customers WHERE rowid = 5")

conn.commit()

c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)

# close our connection
conn.close()
