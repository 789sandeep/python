# Q.4.Why LookupError class is used? Explain with an example KeyError and IndexError.
# Ans.4.
# The LookupError class is a base class for exceptions that occur when a specified key or index cannot be found in a collection or sequence. It is a subclass of the built-in Exception class.

# Two common subclasses of LookupError are KeyError and IndexError.

# KeyError is raised when you try to access a dictionary key that doesn't exist. For example:
try:
    my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
    print(my_dict["hello"])  # Raises a KeyError, because 'hello' isn't in the dictionary
except KeyError as e:
    print(e)

# IndexError is raised when you try to access a list or tuple element that doesn't exist. For example:
try:
    my_list = ['apple', 'banana', 'orange']
    print(my_list[3])  # Raises an IndexError, because there is no fourth element in the list
except IndexError as e:
    print(e)
# Both KeyError and IndexError are subclasses of LookupError, because they occur when you try to look up an element that isn't present in the collection or sequence.