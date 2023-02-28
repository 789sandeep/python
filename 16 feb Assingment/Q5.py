# Q5. Explain Primary Key and Foreign Key.

# Primary key and foreign key are both important concepts in relational databases.

# A primary key is a column or set of columns in a table that uniquely identifies each row in the table. It must have a unique value for each row, and it cannot have null values. Primary keys are used to enforce data integrity and ensure that each record in the table can be uniquely identified. They can also be used as a reference for other tables.

# A foreign key, on the other hand, is a column or set of columns in one table that refers to the primary key of another table. It establishes a relationship between two tables, with the foreign key in one table referencing the primary key in the other table. The foreign key can have null values, but it must match an existing value in the referenced primary key column of the other table.

# Foreign keys are used to ensure referential integrity, which means that the data in one table depends on the data in another table. They are also used to enforce business rules and maintain data consistency across tables. For example, if you have a customer table and an order table, the order table might have a foreign key that references the primary key of the customer table, ensuring that each order is associated with a valid customer.

# In summary, primary keys uniquely identify records in a table, while foreign keys establish relationships between tables and ensure referential integrity.