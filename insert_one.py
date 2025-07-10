import sqlite3

# make a connection to the database
conn = sqlite3.connect('sqlite3/customer.db')

# make a connection to a TEMPORARY database
# conn = sqlite3.connect(':memory:')

# Create a cursor
c = conn.cursor()

# insert data into database
c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")

# commit our commands
conn.commit()

# close our connection
conn.close()
