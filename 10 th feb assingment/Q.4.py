# Q4. Explain the following with python code: read(), readline() and readlines().
#Ans.4.In Python, there are different methods to read the contents of a file. Here's how you can use read(), readline(), and readlines() to read the contents of a file:

# read() method:
# The read() method reads the entire contents of a file as a single string. You can pass an optional parameter to specify the maximum number of characters to read.

# Here's an example that demonstrates how to use the read() method:

# Open the file in read mode
f = open("read.txt", "r")

# Read the entire contents of the file
content = f.read()

# Print the contents of the file
print(content)

# Close the file
f.close()
# readline() method:
# The readline() method reads a single line from the file and returns it as a string. It moves the file pointer to the next line after the line that was just read.

# Here's an example that demonstrates how to use the readline() method:

# Open the file in read mode
f = open("read.txt", "r")

# Read the first line of the file
line1 = f.readline()

# Print the first line of the file
print(line1)

# Read the second line of the file
line2 = f.readline()

# Print the second line of the file
print(line2)

# Close the file
f.close()
# readlines() method:
# The readlines() method reads all the lines of the file and returns them as a list of strings. Each string in the list represents a single line from the file.

# Here's an example that demonstrates how to use the readlines() method:


# Open the file in read mode
f = open("read.txt", "r")

# Read all the lines of the file
lines = f.readlines()

# Print all the lines of the file
for line in lines:
    print(line)

# Close the file
f.close()
# In all of the above examples, we open the file using the open() method, then read the contents of the file using one of the above methods, and finally close the file using the close() method to free up system resources.