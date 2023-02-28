# Q.2. What happens when an exception is not handled? Explain with an example.
# Ans.2.
# When an exception is not handled in Python, it will cause the program to terminate with an error message. The error message will contain information about the type of exception that occurred, along with a traceback that shows the call stack at the point where the exception was raised.

# Here's an example to illustrate what happens when an exception is not handled:

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Please enter only integers")
# In this code, we're asking the user to enter two numbers, and then we're dividing the first number by the second number. If the user enters a non-integer value, we catch the ValueError exception and print an error message.

# However, if we don't handle the exception and the user enters a 0 as the second number, the program will raise a ZeroDivisionError exception. Since we haven't provided a catch block for this exception, the program will terminate and print an error message: