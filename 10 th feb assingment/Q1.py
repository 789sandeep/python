# Q.1.Which function is used to open a file? What are the different modes of opening a file? Explain each mode of file opening.
# In Python, the built-in open() function is used to open a file.

# Syntax: open(filename, mode)

# The open() function takes two arguments:

# filename: name of the file to be opened (including the path, if the file is not in the current working directory).
# mode: specifies the purpose of opening the file.
# The different modes of opening a file in Python are:

# r - Read mode: This mode opens a file for reading only. The file pointer is placed at the beginning of the file. If the file does not exist, an error is raised.

# w - Write mode: This mode opens a file for writing only. The file pointer is placed at the beginning of the file, and the contents of the file are truncated. If the file does not exist, a new file is created.

# a - Append mode: This mode opens a file for writing only. The file pointer is placed at the end of the file. If the file does not exist, a new file is created.

# x - Exclusive creation mode: This mode creates a new file for writing only. If the file already exists, an error is raised.

# b - Binary mode: This mode is used for working with binary files, such as image or audio files.

# t - Text mode: This mode is used for working with text files, such as CSV or text documents.

# + - Update mode: This mode opens a file for both reading and writing.

# To open a file in a specific mode, you need to pass the mode as the second argument to the open() function. For example:


# Open a file in read mode
f = open("file.txt", "r")

# Open a file in write mode
f = open("file.txt", "w")

# Open a file in append mode
f = open("file.txt", "a")

# Open a file in exclusive creation mode
# f = open("file.txt", "x")

# Open a binary file
# f = open("file.bin", "rb")

# Open a text file
f = open("file.txt", "rt")

# Open a file in update mode
f = open("file.txt", "r+")

# It is important to note that after opening a file, you should always close it using the close() method to free up system resources.