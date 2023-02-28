# Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.
# To connect MySQL to Python, we need to use a Python module called mysql-connector-python. You can install this module using pip, by running the following command in your terminal or command prompt:

# Copy code
# pip install mysql-connector-python
# Once you have installed the mysql-connector-python module, you can use the following Python code to connect to your MySQL database

import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a SQL query
mycursor.execute("SELECT * FROM customers")

# Fetch the result
result = mycursor.fetchall()

# Print the result
for row in result:
  print(row)
# In the code above, we first import the mysql.connector module. We then use the connect() method of the mysql.connector module to connect to the MySQL database. The connect() method takes several arguments, including the host, user, password, and database name.

# Once we have connected to the database, we create a cursor object using the cursor() method of the mydb object. The cursor is used to execute SQL queries and fetch the result.

# The execute() method is used to execute a SQL query. The query is passed as a string argument to the execute() method. The fetchall() method is then used to fetch all the rows returned by the query. The result is stored in the result variable, which is then printed using a for loop.

# The execute() method can also be used to execute other types of SQL queries, such as INSERT, UPDATE, and DELETE. For example, to insert a new row into the customers table, you can use the following code:

# Insert a new row
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

# Commit the transaction
mydb.commit()

# print(mycursor.rowcount, "record inserted.")
# In this code, we first define an SQL query to insert a new row into the customers table. The query includes placeholders %s for the values we want to insert. We then define a tuple val that contains the values we want to insert. The execute() method is then used to execute the query, passing the sql and val variables as arguments.

# After executing the query, we need to commit the transaction using the commit() method of the mydb object. Finally, we print the number of rows that were affected by the query using the rowcount attribute of the mycursor object.

# Overall, the cursor() method is used to create a cursor object, which is used to execute SQL queries and fetch the result. The execute() method is used to execute an SQL query, and the fetchall() method is used to fetch all the rows returned by the query.