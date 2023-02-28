#  Q.1.Explain why we have to use the Exception class while creating a Custom Exception.
# Note: Here Exception class refers to the base class for all the exceptions.

# anS.1.In Python, the Exception class is the base class for all built-in exceptions. When creating a custom exception, it is recommended to inherit from the Exception class. Here are some reasons why:

# Inheritance: Inheriting from the Exception class allows the custom exception to inherit all the standard exception methods and attributes, such as __str__ and args, making it easier to create and handle the exception.

# Consistency: By inheriting from Exception, the custom exception is consistent with other built-in exceptions, making it easier to understand and use. It also ensures that the custom exception will work seamlessly with other exception handling code.

# Clarity: Using the Exception class in the raise statement when raising the custom exception makes it clear that the custom exception is indeed an exception and not a regular Python object. This can help avoid confusion when handling the exception.

# Compatibility: Using the Exception class ensures compatibility with future versions of Python. If Python were to change the base class for exceptions in the future, code that uses the Exception class would still work without any modifications.

# Overall, using the Exception class as the base class for a custom exception provides consistency, clarity, and compatibility, making it easier to create, handle, and maintain the exception in Python.