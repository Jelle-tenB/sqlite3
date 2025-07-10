import sqlite3

# make a connection to the database
conn = sqlite3.connect('sqlite3/customer.db')

# Create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT * FROM customers")

# get items
# get items within the tuple
# print(c.fetchone()[0])
# c.fetchmany(3)
items = c.fetchall()

for item in items:
    # \t stands for TAB
    print(item[0] + " " + item[1] + "\t" + item[2])

# commit our commands
conn.commit()

# close our connection
conn.close()
