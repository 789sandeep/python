# Q.4.Explain with an example:

# a. try and else

# b. finally

# c. raise

# Ans.4.
#a. try and else:
# In Python, you can use the else statement with the try statement to specify a block of code to execute if no exceptions are raised in the try block. Here's an example:

import logging
logging.basicConfig(filename="error1.log",level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s")
try:
    logging.info("i am try")
    num1 = int(input("Enter a number: "))
    logging.info("user enter the value name variable is num1")
    num2 = int(input("Enter another number: "))
    logging.info("user enter the another number variable name is num2")
    result = num1 / num2
    logging.info("result variable store a value both divisible num1 by num2")
except ValueError:
    logging.info("this is except a value error")
    print("Please enter only integers")
else:
    logging.info("when this statement is excute befor all  the properties excute try ")
    print("Result:", result)

# In this example, we're asking the user to enter two numbers, and then we're dividing the first number by the second number. If the user enters a non-integer value, the program will jump to the except block and print an error message. If the user enters valid inputs, the program will execute the code in the else block and print the result of the division.

# b. finally:
# In Python, you can use the finally statement with the try statement to specify a block of code to execute regardless of whether an exception was raised or not. Here's an example:

try:
    file = open("example.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()
# In this example, we're trying to open a file called "example.txt" for reading. If the file is found, we'll read the contents of the file into the data variable. If the file is not found, we'll jump to the except block and print an error message. Regardless of whether an exception was raised or not, the finally block will execute and close the file.

# c. raise:
# In Python, you can use the raise statement to raise an exception manually. Here's an example:

def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return num1 / num2

try:
    result = divide(10, 0)
except ZeroDivisionError as error:
    print(error)
# In this example, we're defining a function called divide that takes two arguments and returns their division result. If the second argument is 0, we raise a ZeroDivisionError with a custom error message. We then call the divide function with 10 and 0 as arguments, which will raise a ZeroDivisionError. We catch the exception using the except block and print the error message.

# Using the raise statement allows you to create custom exceptions and raise them when needed, which can be useful for handling specific errors in your program.



