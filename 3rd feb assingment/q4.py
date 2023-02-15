# Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator function.

# In Python, a generator function is a special type of function that allows you to generate a sequence of values on the fly, as opposed to generating them all at once and storing them in memory. Generator functions use the yield keyword to return values one at a time, rather than returning a whole sequence all at once.

# The yield keyword allows a generator function to pause its execution and return a value to the caller. When the function is called again, it picks up where it left off and continues executing from the point it paused, remembering the state of its local variables.

# Here's an example of a generator function that generates a sequence of even numbers up to a certain limit:

def generate_numbers(limit):
    for i in range(1, limit, 1):
        yield i*2
# You can call this function to generate a sequence of even numbers like this:

for number in generate_numbers(11):
    print(number)

# This will output the even numbers from 0 to 8, since we specified a limit of 10.

# The yield keyword allows us to generate these numbers one at a time, rather than generating them all at once and storing them in memory. This is particularly useful when generating large sequences of values that would be impractical to store in memory all at once.

# Generator functions are particularly useful when working with large datasets, as they allow you to generate data on the fly, rather than loading everything into memory at once. They can also be more efficient than traditional functions for generating sequences of values, since they don't need to store the entire sequence in memory at once.