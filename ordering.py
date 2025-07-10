import sqlite3

# make a connection to the database
conn = sqlite3.connect('sqlite3/customer.db')

# Create a cursor
c = conn.cursor()

# Query the database - ORDER BY
# ASCending
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid")

# DESCending
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")

# order by last name
c.execute("SELECT rowid, * FROM customers ORDER BY last_name")

items = c.fetchall()

for item in items:
    print(item)

# close our connection
conn.close()
