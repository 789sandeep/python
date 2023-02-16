# Q1. Create a python program to sort the given list of tuples based on integer value using a lambda function.
l=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
l.sort(key=lambda x:x[1])
print(l) 
