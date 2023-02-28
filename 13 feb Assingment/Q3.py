# Q.3.What errors are defined in the ArithmeticError class? Explain any two with an example.
# Ans.3.
# The ArithmeticError class is a built-in exception class in Python that is used to represent errors that occur during arithmetic operations. It is a subclass of the Exception class and is itself a superclass for several other exception classes that are used to represent more specific arithmetic errors.

# Here are two examples of specific exceptions that are defined in the ArithmeticError class:

# ZeroDivisionError: This exception is raised when a division operation is attempted with a denominator of zero. For example:

num1 = 10
num2 = 0

try:
    result = num1 / num2
except ZeroDivisionError as error:
    print("hii",error)
# This code will raise a ZeroDivisionError exception, which will be caught by the except block and print the error message "division by zero".

# OverflowError: This exception is raised when an arithmetic operation exceeds the maximum representable value for a given data type. For example:

import sys

max_int = sys.maxsize

try:
    result = max_int + 1
    print(result)
except OverflowError as error:
    print(error)
# This code will raise an OverflowError exception, which will be caught by the except block and print the error message "Python int too large to convert to C long".

# By catching and handling specific exceptions like ZeroDivisionError and OverflowError, we can handle errors in our code in a more fine-grained way, allowing us to provide more informative error messages to users and take appropriate actions to address the errors.