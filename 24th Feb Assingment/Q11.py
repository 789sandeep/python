# Q11. You have a Pandas DataFrame df with a column 'Date'. Write a Python function that creates a new column 'Weekday' in the DataFrame. The 'Weekday' column should contain the weekday name (e.g.Monday, Tuesday) corresponding to each date in the 'Date' column.

import pandas as pd
def days(df):
    df['Weekday']=['Sunday',' Monday', 'Tuesday', 'Wednesday', 'Thursday']
    return df
    
data6={"Date":['2023-01-01','2023-01-02','2023-01-03','2023-01-04','2023-01-05']}
df=pd.DataFrame(data6)
print(days(df))