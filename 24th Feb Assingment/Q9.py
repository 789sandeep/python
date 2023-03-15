# Q9. Given a Pandas DataFrame df with a column 'Values', write a Python function to calculate the mean,median, and standard deviation of the values in the 'Values' column.
import pandas as pd
def calculate(df):
    print(df.mean())
    print(df.median())
    print(df.std())
data6={"values":[0 ,3 ,5 ,1]}
df=pd.DataFrame(data6)
calculate(df)