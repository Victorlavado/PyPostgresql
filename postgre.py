import psycopg2
# Import psycopg2  library to interact with PostgreSQL databases

def create_table():
    # Function to create a table in a database and add some data
    conn = psycopg2.connect("dbname= 'database1' user= 'postgres' password='postgres123' host= 'localhost' port='5432'")
    # Establish the connection and store the connect method into conn
    # variable
    cur = conn.cursor()
    # Create a cursor object and store into cur variable
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # SQL query: in case there is no table called "store" then create it with
    # item, quantity and price columns whose data types are TEXT, INTEGER and
    # REAL respectively
    cur.execute("INSERT INTO store VALUES ('Wine Glass',8,10.5)")
    # Execute method to add new data into the store table following the
    # format previously defined for the columns
    conn.commit()
    # Commit the changes made
    conn.close()
    # Close the connection

def insert(item,quantity,price):
    # Function that takes as parameters the values that you pass to insert
    # them into "store" table
    conn = psycopg2.connect("dbname= 'database1' user= 'postgres' password='postgres123' host= 'localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)" , (item,quantity,price))
    # (%s,%s,%s) represents the variable that will substitued by
    # the parameters input to the function insert
    conn.commit()
    conn.close()

def view():
    # Function that selects data from the table, so it can be displayed
    conn = psycopg2.connect("dbname= 'database1' user= 'postgres' password='postgres123' host= 'localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    # The excute methos selects all the data from "store" table
    rows = cur.fetchall()
    # The data selected is then fetched and stored into rows variable
    conn.close()
    return rows
    # The view function returns the rows variable, so when it is called by
    # print() it can be displayed

def delete(item):
    # Function that deletes data from the table
    conn = psycopg2.connect("dbname= 'database1' user= 'postgres' password='postgres123' host= 'localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    # The row is selected by defining the item value and then it is deleted
    # (item,) with its final comma is necessary to avoid error is psycopg2
    # library
    conn.commit()
    conn.close()

def update(quantity,price,item):
    # Function that updates existing data from the table
    conn = psycopg2.connect("dbname= 'database1' user= 'postgres' password='postgres123' host= 'localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity,price,item))
    # Execute method updates quantity and price in the specified row that is
    # defined by item
    conn.commit()
    conn.close()

create_table()
insert("Tomato",8,9)
update(11,6,"Tomato")
#delete("Wine Glass")
print(view())
# Call some the functions
