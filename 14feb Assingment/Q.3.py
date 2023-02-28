# Q.3. Explain the following functions
# ( run
#  start
#  join
# ' isAlive)
# The following are the explanations of the functions in the threading module in Python:

# run() - This function is the entry point for the thread's execution. It is called when a new thread is started using the start() method. The run() function contains the code that is executed by the thread.

# start() - This function starts a new thread by calling the run() method of the thread object. When a thread is started using the start() method, it begins executing in the background, and the program continues to run in the main thread.

# join() - This function blocks the program's execution until the thread has completed its execution. When a thread is started using the start() method, it runs in the background, and the program continues to execute in the main thread. The join() method can be used to wait for the thread to complete its execution before continuing the program's execution.

# isAlive() - This function returns a Boolean value indicating whether the thread is still active. A thread is considered active if it has been started and has not yet completed its execution. The isAlive() method can be used to check the status of a thread and determine if it is still running.

# Overall, these functions are used to create, start, and manage threads in a Python program. The run() and start() methods are used to start the execution of a new thread, while the join() method is used to wait for a thread to complete its execution. The isAlive() method is used to check the status of a thread and determine if it is still running.