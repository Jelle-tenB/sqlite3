import sqlite3

# make a connection to the database
conn = sqlite3.connect('sqlite3/customer.db')

# Create a cursor
c = conn.cursor()

# Query the database for specific item
# c.execute("SELECT * FROM customers WHERE last_name = 'Elder'")

# Query the database for item which STARTS with Br but ends in anything
# c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'")

# Query database for item that ENDS with codemy.com
c.execute("SELECT * FROM customers WHERE email LIKE '%codemy.com'")

# get items
# c.fetchone()
# c.fetchmany(3)
items = c.fetchall()

for item in items:
    print(item)

# commit our commands
conn.commit()

# close our connection
conn.close()