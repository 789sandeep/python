# Q1. List any five functions of the pandas library with execution.
import pandas as pd
# read_csv: This function is used to read data from a CSV file and return a DataFrame object.
df=pd.read_csv("df.csv")
df1=pd.read_csv("df1.csv")
# groupby() - This function groups a DataFrame by one or more columns.
group=df1.groupby(["name"])["age"].mean()
# merge(): This function is used to merge two DataFrames based on a common column.
merg1=pd.merge(df,df1,on="age")
# fillna() - This function fills missing values in a DataFrame with a specified value.
fila=df1.fillna(3)
# head() - This function returns the first n rows of a DataFrame.
top_4=df1.head()
print(df,"\n\n")
print(group,"\n\n")
print(merg1,"\n\n")
print(fila,"\n\n")
print(top_4)