# Q.4.check how many times a given number can be divided by 3 before it is less than or equal to 10
num = 243
count = 0

while num > 10:
    num = num // 3
    count += 1

print("The given number can be divided by 3", count, "times before it is less than or equal to 10.")
