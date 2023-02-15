# Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,16, 18, 20].
# Ans.3.An iterator in Python is an object that can be iterated (looped) upon. It is used to represent a stream of data.
# To create an iterator object, we use the built-in iter() method, and to iterate over the object we use the next() method.
a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for i in range(0,len(a)):
    if i<5:
      print(a[i])