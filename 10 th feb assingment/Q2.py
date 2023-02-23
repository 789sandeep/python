# Q.2.Why close() function is used? Why is it important to close a file?
#Ans.2. The close() method is used to close an opened file in Python. It is important to close a file after you are done using it because it frees up system resources (such as file descriptors) that were being used by the program.

# If you open a file and do not close it, the operating system may not immediately release the resources allocated to that file, leading to resource leaks, which can ultimately cause issues such as file corruption, decreased performance, and even system crashes.

# When you use the close() method, any data that is still in the buffer will be written to the file before it is closed, so you don't lose any data. Also, once a file has been closed, you cannot perform any more operations on it until it is opened again.

# Here's an example that demonstrates why it's important to close a file after using it:

# Open a file in write mode
f = open("example.txt", "w")

# Write some data to the file
f.write("Hello, world!")

# Oops, we forgot to close the file!
# f.close()

# The file may still be locked, preventing other programs from accessing it.

# ... some time later, we try to open the file again
f = open("example.txt", "r")
# This will result in an error because the file is still open in write mode.

# Close the file to release the resources
f.close()
# In summary, closing a file using the close() method ensures that the file is properly saved, frees up system resources, and prevents any issues that can arise from leaving a file open.