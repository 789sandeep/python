user=int(input("enter the number:"))
t1=0
t2=1
next_value=0
i=1
while i<=user:
    if(i==1):
        print(t1)
    elif(i==2):
        print(t2)
    next_value=t1+t2
    t1=t2
    t2=next_value
    print(next_value)
    i=i+1