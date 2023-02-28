# Q.3.Which Python statements are used to catch and handle exceptions? Explain with an example.
# Ans.3.
# In Python, the try and except statements are used to catch and handle exceptions. The try block contains the code that might raise an exception, and the except block contains the code to handle the exception.

# Here's an example to illustrate how to catch and handle an exception in Python using try and except statements:

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Please enter only integers")
except ZeroDivisionError:
    print("Cannot divide by zero")

# In this code, we're asking the user to enter two numbers, and then we're dividing the first number by the second number. We use the try statement to enclose the code that might raise an exception. If an exception occurs, Python will jump to the corresponding except block and execute the code there.

# In this example, we have two except blocks. The first one catches ValueError exceptions, which are raised when the user enters a non-integer value. The second one catches ZeroDivisionError exceptions, which are raised when the user enters 0 as the second number.

# If the user enters a non-integer value, the program will jump to the first except block and print the error message. If the user enters 0 as the second number, the program will jump to the second except block and print the error message. If the user enters valid inputs, the program will execute normally and print the result of the division.

# Using try and except statements to catch and handle exceptions is a good practice in Python, as it allows your program to gracefully handle errors and continue executing, rather than crashing with an error message.