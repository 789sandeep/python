# Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the range of 1 to 25.
def odd_value(a):
    l1=[]
    for i in range(1,a):
        if i%2 !=0:
            l1.append(i)
    return l1
b=int(input("enter the number:"))
print(odd_value(b))