# Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.

# In Pandas, a DataFrame is a 2-dimensional labeled data structure with columns of potentially different types, similar to a spreadsheet or a SQL table. It is essentially a collection of Pandas Series objects that share the same index.

# A Pandas Series, on the other hand, is a one-dimensional labeled array that can hold data of any type (integer, float, string, etc.). Each element in a Series is assigned a unique index, which can be used to access individual elements.
import panda as pd
import csv
data_frame=[["name","age","gender"],
           ["alice",25,"female"],
           ["bob",30,"male"],
           ["clair",30,"female"]]
with open("df.csv","w") as f:
    write=csv.writer(f)
    for i in data_frame:
        write.writerow(i)
data=pd.read_csv("df.csv")
print(data)
print(data[["age"]])
print(type(data[["age"]]))
print(type(data["age"]))
print(data["age"])