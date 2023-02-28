# Q.6.Create a custom exception class. Use this class to handle an exception.
# Ans.6.
# Sure, here's an example of how to create a custom exception class and use it to handle an exception:
import logging
logging.basicConfig(filename="error.log",level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s")
class CustomException(Exception):
    logging.info("this is the customException class")
    pass

def divide(num1, num2):
    logging.info("this is divide function name")
    if num2 == 0:
        logging.info("if statement check num2 is equal to 0")
        raise CustomException("Cannot divide by zero")
    else:
        logging.info("this is the else statement")
        return num1 / num2

try:
    logging.info("i am try function")
    result = divide(10, 0)
except CustomException as error:
    logging.info("handle the error")
    print(error)
logging.info("end of the program")
# In this example, we define a custom exception class called CustomException that inherits from the built-in Exception class. We then define a divide function that takes two numbers as input and returns their division result. If the second argument is 0, we raise a CustomException with a custom error message.

# We then call the divide function with 10 and 0 as arguments, which will raise the CustomException. We catch the exception using the except block and print the error message.

# Using custom exception classes like CustomException allows us to create more specific and informative error messages, making it easier to understand and handle errors in our code. We can also use different custom exception classes for different scenarios, allowing us to handle errors in a more fine-grained way.



