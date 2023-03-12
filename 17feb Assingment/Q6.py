# Q6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB
# The sort() method in MongoDB is used to sort the documents in a collection based on a specified field or fields. The method takes one or more parameters that specify the sorting order and direction.

# Here is an example to demonstrate sorting in MongoDB using the sort() method:

# import MongoClient from pymongo library
from pymongo import MongoClient

# connect to MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# sort documents by age field in ascending order
results = collection.find().sort('age', 1)

# print the results
for result in results:
    print(result)
# In the code above, we first import the MongoClient class from the pymongo library to establish a connection to the MongoDB database. We then specify the name of the database and collection that we want to sort.

# Next, we call the find() method on the collection object without any parameters to retrieve all documents in the collection. We then call the sort() method on the resulting cursor object and pass in the field name that we want to sort on (age) and the sorting direction (1 for ascending order, -1 for descending order).

# Finally, we iterate over the sorted results and print each document.

# Note that the sort() method can also accept multiple fields to sort on. In this case, the fields are specified as a list of tuples, where each tuple contains the field name and the sorting direction. For example:

# bash
# Copy code
# # sort documents by age field in ascending order and then by name field in descending order
# results = collection.find().sort([('age', 1), ('name', -1)])
# This will sort the documents first by the age field in ascending order and then by the name field in descending order.