# Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
# function.
l=['python', 'php', 'aba', 'radar', 'level','heloo','sanas']
a=list(filter(lambda x:x==x[::-1],l))
print(a)