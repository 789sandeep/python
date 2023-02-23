# Q6. Explain the write() and writelines() functions. Give a suitable example.
#Ans.6. In Python, the write() and writelines() functions are used to write data to a file.

# write() function:
# The write() function writes a string to the file. If the file already exists, the new data will be appended to the end of the file. If the file does not exist, a new file will be created.

# Here's an example of how to use the write() function to write a string to a file:

# Open the file in write mode
f = open("writes.txt", "w")

# Write a string to the file
f.write("This is some text that we are writing to the file.")

# Close the file
f.close()
# In this example, we open the file in write mode, use the write() function to write a string to the file, and then close the file.

# writelines() function:
# The writelines() function writes a list of strings to the file. Each string in the list represents a single line of text, and the function adds a newline character after each string.

# Here's an example of how to use the writelines() function to write a list of strings to a file:

# makefile
# Copy code
# Open the file in write mode
f = open("writes.txt", "w")

# Write a list of strings to the file
lines = ["This is the first line.", "This is the second line.", "This is the third line."]
f.writelines(lines)

# Close the file
f.close()
# In this example, we open the file in write mode, create a list of strings representing each line of text, use the writelines() function to write the list to the file, and then close the file.

# Note that the write() and writelines() functions can also be used with the with statement for more concise and safe file handling. Here's an example:


# Open the file using the with statement
with open("read.txt", "w") as f:

    # Write a string to the file
    f.write("This is some text that we are writing to the file.")

    # Write a list of strings to the file
    lines = ["This is the first line.", "This is the second line.", "This is the third line."]
    f.writelines(lines)

# The file is automatically closed when the with block is exited
# In this example, we use the with statement to open the file, write a string and a list of strings to the file using the write() and writelines() functions, and then close the file automatically when the block of code inside the with statement is exited.