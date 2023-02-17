# Q.5.why and when o use while loop in python give a details description with example
#  "while" loop in Python is used to execute a block of code repeatedly as long as a certain condition is true. The condition is checked at the beginning of each iteration, and if it is true, the loop body is executed. The loop continues until the condition becomes false.


# The condition can be any expression that evaluates to a Boolean value (True or False). The loop body can contain any number of statements.

# Here's an example of using a while loop in Python to print the first 5 even numbers:

n = 0
count = 0
while count < 5:
    if n % 2 == 0:
        print(n)
        count += 1
    n += 1
# In this example, the condition is count < 5. The loop continues until the count variable is equal to 5. Inside the loop body, the if statement checks if n is even. If it is, the number is printed and count is incremented. Finally, n is incremented to check the next number.