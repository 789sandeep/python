# Q5. Explain why with statement is used with open(). What is the advantage of using with statement and open() together?
#Ans.5. The with statement is used with the open() function to ensure that a file is properly closed after it has been used. It provides a convenient way to handle files without having to explicitly call the close() method.

# Here's an example of how to use the with statement with the open() function:

# Open the file using the with statement
with open("read.txt", "r") as f:

    # Read the contents of the file
    content = f.read()

    # Print the contents of the file
    print(content)

# The file is automatically closed when the with block is exited
# When you use the with statement, Python automatically closes the file when the block of code inside the with statement is exited, even if an exception occurs. This helps to ensure that the file is properly closed and prevents issues such as resource leaks.

# The advantage of using the with statement with the open() function is that it makes your code more concise, more readable, and less error-prone. You don't have to worry about closing the file manually, which reduces the risk of making mistakes. Additionally, using the with statement can be more efficient because it ensures that the file is closed as soon as it is no longer needed, which frees up system resources.

# In summary, using the with statement with the open() function provides a convenient and reliable way to handle files in Python, and helps to ensure that files are properly closed after they have been used.