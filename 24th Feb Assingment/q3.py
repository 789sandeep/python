# Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
# function should print the sum to the console.
# For example, if the 'Values' column of df contains the values [10, 20, 30, 40, 50], your function should
# calculate and print the sum of the first three values, which is 60.
import pandas as pd
def sum_cal(df):
    sum=0
    for i in range(0,3):
         sum=sum+df["values"][i]
    return sum              
data1={"values":[10,20,30,40,50]}
df=pd.DataFrame(data1)
obj=sum_cal(df)
print(obj)