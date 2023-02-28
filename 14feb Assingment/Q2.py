# Q.2.hy threading module used? rite the use of the following functions
# ( activeCount
#  currentThread
#  enumerate).

#  The threading module in Python is used to implement multithreading in a Python program. It provides a simple and efficient way to create and manage threads. The primary purpose of using the threading module is to improve the performance of a program by executing multiple tasks simultaneously, thereby utilizing the system resources more efficiently.

# The following are the uses of the three functions in the threading module:

# activeCount() - This function returns the number of thread objects that are active in the current process. An active thread is a thread that has been started but has not yet been terminated.

# currentThread() - This function returns a reference to the thread object representing the current thread of execution. The thread object has various attributes, including its name, identification number, and state.

# enumerate() - This function returns a list of all thread objects that are active in the current process. Each item in the list is a reference to a thread object, and the list includes the main thread as well.

# Overall, these functions are used to manage and inspect the threads in a Python program, such as determining how many threads are currently active, identifying the current thread of execution, and getting a list of all the threads that are active in the program.

