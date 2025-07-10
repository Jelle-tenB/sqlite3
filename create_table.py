import sqlite3

# make a connection to the database
conn = sqlite3.connect('sqlite3/customer.db')

# make a connection to a TEMPORARY database
# conn = sqlite3.connect(':memory:')

# Create a cursor
c = conn.cursor()

# create a table
# DO NOT END WITH A COMMA
c.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email text
    )""")

c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')")

# DATATYPES:
# NULL
# INTEGER
# REAL , decimal numbers
# TEXT
# BLOB , stored as is; like an images

# commit our commands
conn.commit()

# close our connection
conn.close()
