import sqlite3

# make a connection to the database
conn = sqlite3.connect('sqlite3/customer.db')

# Create a cursor
c = conn.cursor()

# Update Records
# Change the first name to Bob when the last name is Elder
# c.execute("""UPDATE customers SET first_name = 'Bob'
        #   WHERE last_name = 'Elder'
        #   """)

c.execute("""UPDATE customers SET first_name = 'John'
          WHERE rowid = 1
          """)

conn.commit()

c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)

# close our connection
conn.close()
