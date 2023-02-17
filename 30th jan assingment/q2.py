user=int(input("enter the cost price:"))
if user>100000:
    print("15%")
elif user>50000 and user<=100000:
    print("10%")
else:
    print("5%")