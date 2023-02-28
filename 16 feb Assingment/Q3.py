 # Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.
 
# A3. DML stands for Data Manipulation Language, which is a subset of SQL used to manipulate the data stored in a database. DML statements are used to insert, update, retrieve, and delete data in a database.

# The three commonly used DML statements are:

# INSERT: The INSERT statement is used to insert new data into a table. For example, the following SQL statement inserts a new record into the "employees" table:

# INSERT INTO employees (id, name, department, salary)
# VALUES (1, 'John Smith', 'Sales', 50000);

# This statement adds a new employee record with an ID of 1, a name of "John Smith", a department of "Sales", and a salary of 50000.

# UPDATE: The UPDATE statement is used to modify existing data in a table. For example, the following SQL statement updates the salary of the employee with an ID of 1:

# UPDATE employees
# SET salary = 60000
# WHERE id = 1;

# This statement updates the salary of the employee with an ID of 1 to 60000.

# DELETE: The DELETE statement is used to remove data from a table. For example, the following SQL statement removes the employee with an ID of 1 from the "employees" table:

# DELETE FROM employees
# WHERE id = 1;

# This statement deletes the employee with an ID of 1 from the table.

# These DML statements are essential for managing the data stored in a database. INSERT is used to add new data, UPDATE is used to modify existing data, and DELETE is used to remove data. Together with DDL statements, DML statements form the core of SQL and are essential for managing a database.