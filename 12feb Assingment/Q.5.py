# Q5. What are Custom Exceptions in python? Why do we need Custom Exceptions? Explain with an example.
# Ans..5
# In Python, you can create your own custom exceptions by defining a new class that inherits from the built-in Exception class or one of its subclasses. Custom exceptions can be used to handle specific errors in your program that are not covered by the built-in exceptions.

# We need custom exceptions in Python for several reasons, including:

# To provide more detailed error messages to users, making it easier for them to understand what went wrong.
# To allow for more fine-grained error handling in our code, allowing us to handle specific errors in different ways.
# To organize our code and make it more readable, by grouping related exceptions into custom exception classes.
# Here's an example of how to define a custom exception in Python:

class NegativeNumberError(Exception):
    def __init__(self, message="Number cannot be negative"):
        self.message = message
        super().__init__(self.message)

def square_root(num):
    if num < 0:
        raise NegativeNumberError
    else:
        return num ** 0.5

try:
    result = square_root(-10)
except NegativeNumberError as error:
    print(error)

# In this example, we define a custom exception called NegativeNumberError that is raised when a negative number is passed to the square_root function. The NegativeNumberError class inherits from the built-in Exception class and defines a custom error message that is printed when the exception is raised.

# We then define a square_root function that takes a number as input and calculates its square root. If the input is negative, we raise a NegativeNumberError exception using the raise statement. We then call the square_root function with -10 as an argument, which will raise the NegativeNumberError. We catch the exception using the except block and print the error message.

# Using custom exceptions like NegativeNumberError allows us to handle specific errors in our code in a more organized and readable way. We can create custom exceptions for different scenarios and handle them appropriately, making our code more robust and easier to maintain.