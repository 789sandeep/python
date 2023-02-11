user=int(input("enter the number:"))
bill=0.0
if(user>300):
    bill=bill+(100*4.5)
    user=user-100
    bill=bill+(100*6)

    user=user-100
    bill=bill+(100*10)
    user=user-100
    bill=bill+(user*20)
print("total bill:",bill)
