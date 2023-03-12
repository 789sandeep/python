# Q3. Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.

# To connect to MongoDB in Python, you can use the PyMongo library which provides tools for working with MongoDB. Here's how you can connect to MongoDB, create a database and a collection in Python:


import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database
db = client["mydatabase"]

# Create a collection
col = db["mycollection"]

# This code connects to MongoDB running on the local machine, creates a database named "mydatabase", and a collection named "mycollection" inside it.

# Note that if the database or collection does not already exist, MongoDB will create it when you first add data to it.