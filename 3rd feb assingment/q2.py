# Q.2.Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
# # to demonstrate their use.

# *args and **kwargs are used to pass a variable number of arguments to a function.

# *args allows you to pass a variable number of non-keyword arguments to a function, while **kwargs allows you to pass a variable number of keyword arguments to a function.

# Here's an example of a function that uses *args to print out all of the arguments passed to it:

def print_args(*args):
    for arg in args:
        print(arg)
# You can call this function with any number of arguments, like this:

print_args(1,24,64)
# Here's an example of a function that uses **kwargs to print out all of the key-value pairs passed to it:
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# You can call this function with any number of keyword arguments, like this:
print_kwargs(name="fdfjhj", age=30, city="New York",course="data science")