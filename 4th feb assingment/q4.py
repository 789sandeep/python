# Q4. Write a python program using reduce function to compute the product of a list containing numbers
# from 1 to 25.
from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
a=reduce(lambda x,y:x*y,l)
print(a)