# Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.
# A2. DDL stands for Data Definition Language, which is a subset of SQL used to define and manage the structure of a database. DDL statements are used to create, modify, and delete database objects such as tables, indexes, and views.

# The four commonly used DDL statements are:

# CREATE: The CREATE statement is used to create new database objects, such as tables, indexes, or views. For example, the following SQL statement creates a new table called "employees" with columns for employee ID, name, and department:

# CREATE TABLE employees (
# id INT PRIMARY KEY,
# name VARCHAR(50),
# department VARCHAR(50)
# );

# DROP: The DROP statement is used to delete an existing database object, such as a table or view. For example, the following SQL statement drops the "employees" table:

# DROP TABLE employees;

# ALTER: The ALTER statement is used to modify the structure of an existing database object, such as adding or deleting columns from a table. For example, the following SQL statement adds a new column "salary" to the "employees" table:

# ALTER TABLE employees
# ADD salary DECIMAL(10, 2);

# TRUNCATE: The TRUNCATE statement is used to delete all data from an existing table, but the table structure remains intact. For example, the following SQL statement deletes all data from the "employees" table:

# TRUNCATE TABLE employees;

# These DDL statements are essential for managing the structure and contents of a database. CREATE is used to create new tables and other objects, DROP is used to remove them, ALTER is used to change the structure of tables and objects, and TRUNCATE is used to clear data from tables while retaining their structure.
