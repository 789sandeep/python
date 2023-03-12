# Q7. Explain why delete_one(), delete_many(), and drop() is used.

# delete_one(), delete_many(), and drop() are methods available in database management systems that allow us to remove documents or collections from a database.

# delete_one() is used to remove a single document from a collection that matches a given filter criteria.
# delete_many() is used to remove multiple documents from a collection that match a given filter criteria.
# drop() is used to remove an entire collection from a database.
# These methods are useful for managing data and maintaining database performance. For example, if we have duplicate or outdated data, we can use delete_one() or delete_many() to remove it from the database, keeping only the most up-to-date information. We can also use drop() to remove an entire collection when we no longer need it, freeing up space and resources on the server.

# However, it is important to use these methods with caution, as deleting data is a permanent action that cannot be undone. Therefore, it is recommended to take backups and be sure about the data that needs to be deleted before executing these methods.