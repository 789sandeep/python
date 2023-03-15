# Q8. You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The function should return a new DataFrame that contains only the selected rows.

import pandas as pd
def find_gre_les(df):
        select_row=df[(df["A"]>5) & (df["B"]<10)]
        return select_row
data4={'A':[0,3,5,1,7,8,9],'B': [1,8,2,7,6,5,4],'C': [2,6,9,4,5,6,3]}
df=pd.DataFrame(data4)
print(find_gre_les(df))