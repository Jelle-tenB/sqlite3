import sqlite3

# Query the DB and return all records
def show_all():
    # make a connection to the database
    conn = sqlite3.connect('sqlite3/ourapp/customer.db')

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


# Add a new record to the table
def add_one(first, last, email):
    conn = sqlite3.connect('sqlite3/ourapp/customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    conn.commit()
    conn.close()