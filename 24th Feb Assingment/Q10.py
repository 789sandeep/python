# Q10. Given a Pandas DataFrame df with a column 'Sales' and a column 'Date', write a Python function to
# create a new column 'MovingAverage' that contains the moving average of the sales for the past 7 days
# for each row in the DataFrame. The moving average should be calculated using a window of size 7 and
# should include the current day.

import pandas as pd
def add_moving_average(df):
    df['MovingAverage'] = df['Sales'].rolling(window=7, min_periods=1).mean()
    return df

data5={"Date":['2023-01-01','2023-01-02','2023-01-03','2023-01-04','2023-01-05'],'Sales':[1,2,3,4,5]}
df=pd.DataFrame(data5)
print(add_moving_average(df))