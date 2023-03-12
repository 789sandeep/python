# Q5. Explain how you can use the find() method to query the MongoDB database. Write a simple code to
# demonstrate this.

# The find() method is used in MongoDB to retrieve documents from a collection. It takes an optional query parameter that specifies the selection criteria for the documents to be returned.

# Here is an example code to demonstrate the use of find() method in querying MongoDB database:

# import MongoClient from pymongo library
from pymongo import MongoClient

# connect to MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# query the collection for documents
query = { 'name': 'John' }
results = collection.find(query)

# print the results
for result in results:
    print(result)

# In the code above, we first import the MongoClient class from the pymongo library to establish a connection to the MongoDB database. We then specify the name of the database and collection that we want to query.

# Next, we define a query parameter that specifies the selection criteria for the documents to be returned. In this example, we want to retrieve all documents where the name field is equal to 'John'.

# Finally, we call the find() method on the collection object and pass in the query parameter. The results are stored in a cursor object, which we iterate over and print each document.

# Note that the find() method returns all documents that match the query criteria. If you only want to retrieve a single document, you can use the findOne() method instead. Additionally, you can use various operators such as $gt, $lt, $in, $or, etc., to specify more complex query criteria.



