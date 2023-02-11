# Q5. Write a program to filter count vowels in the below-given string.
string = "I want to become a data scientist"
vowels="aeiou"
for i in string:
    if(i in vowels):
        print(i)