# Q2. Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the DataFrame with a new index that starts from 1 and increments by 2 for each row.
import pandas as pd

def reindex_dataframe(df):
        new_index = pd.Index(range(1,len(df)*2, 2))
        return df.reset_index(drop=True).set_index(new_index)
data={'A':[0 ,3 ,5 ,1],'B': [1 ,8 ,2 ,7 ],'C': [2 ,6 ,9 ,4]}
print(len(data))
df=pd.DataFrame(data)
print(len(df))
new_df = reindex_dataframe(df)
print(new_df)