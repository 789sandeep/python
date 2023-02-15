a=int(input("enter the number:"))
b=a
ans=0
while(a>0):
    rem=a%10
    ans=(ans*10) + rem
    a=a//10
if(ans==b):
    print("this is palindrome number:",ans)
else:
    print("this is not palindrome number:",ans)
