# Q.4. rite a python program to create two threads. Thread one must print the list of squares and thread
# two must print the list of cubes.

import threading

# Define a function to print the list of squares
def print_squares():
    squares = [x*x for x in range(1, 11)]
    print("List of Squares: ", squares)

# Define a function to print the list of cubes
def print_cubes():
    cubes = [x*x*x for x in range(1, 11)]
    print("List of Cubes: ", cubes)

# Create two threads to execute the two functions concurrently
thread1 = threading.Thread(target=print_squares)
thread2 = threading.Thread(target=print_cubes)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish using the join() method
thread1.join()
thread2.join()

# Print a message indicating the program has finished
print("Program finished.")
