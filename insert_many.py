import sqlite3

# make a connection to the database
conn = sqlite3.connect('sqlite3/customer.db')

# make a connection to a TEMPORARY database
# conn = sqlite3.connect(':memory:')

# Create a cursor
c = conn.cursor()

many_customers = [
    ('Wes', 'Brown', 'Wes@brown.com'),
    ('Steph', 'Kuewa', 'steph@kuewa.com'),
    ('Dan', 'Pas', 'dan@pas.com'),
    ('Tim', 'Smith', 'smith@codemy.com'),
    ('Mary', 'Brown', 'mary@codemy.com')
    ]

# insert MANY data into database with placeholders (?)
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# commit our commands
conn.commit()

# close our connection
conn.close()