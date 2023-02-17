# Q.6.use nested while loop to print 3 different pattenr

#Right triangle
i=1
while i<5:
    j=i
    while j>0:
       print("*",end=" ")
       j=j-1
    print()
    i=i+1
print() 

#below right triangle
j=5
while j>0:
    i=j
    while i>0:
        print("*",end=" ")
        i=i-1
    print()
    j=j-1

n = 5
print()
# Upper half of the diamond
i = 1
while i <= n:
    j = 1
    while j <= n-i:
        print(" ", end="")
        j += 1
    j = 1
    while j <= 2*i-1:
        print("*", end="")
        j += 1
    print()
    i += 1
