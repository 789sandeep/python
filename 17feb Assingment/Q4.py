# Q4. Using the database and the collection created in question number 3, write a code to insert one record,
# and insert many records. Use the find() and find_one() methods to print the inserted record.

# To insert one record in the "customers" collection, we can use the insert_one() method provided by PyMongo library. Similarly, to insert many records in the "customers" collection, we can use the insert_many() method.

# Here is the code to insert one record in the "customers" collection:


import pymango

# connect to MongoDB

client = pymongo.MongoClient("mongodb+srv://sandeepprajapati789:sandeep789@cluster0.m6iuw3e.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db = client['mydatabase']
customers = db['customers']

# insert one record
customer = {"name": "John Doe", "address": "123 Main St", "age": 30}
result = customers.insert_one(customer)

# print the inserted record
print(customers.find_one({"_id": result.inserted_id}))
# Here is the code to insert many records in the "customers" collection:


import pymango

# connect to MongoDB

client = pymongo.MongoClient("mongodb+srv://sandeepprajapati789:sandeep789@cluster0.m6iuw3e.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db = client['mydatabase']
customers = db['customers']

# insert many records
customers_list = [
    {"name": "Jane Doe", "address": "456 Broadway", "age": 25},
    {"name": "Bob Smith", "address": "789 Park Ave", "age": 40},
    {"name": "Alice Johnson", "address": "321 Elm St", "age": 50}
]
result = customers.insert_many(customers_list)

# print the inserted records
for id in result.inserted_ids:
    print(customers.find_one({"_id": id}))
# In both cases, we use find_one() method to print the inserted record(s) by passing the _id of the inserted record(s) as a filter.