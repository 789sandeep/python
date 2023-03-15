# Q4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column 'Word_Count' that contains the number of words in each row of the 'Text' column.
import pandas as pd
data2={"text":[" Braund, Mr. Owen Harris","Montvila, Rev. Juozas","Dooley, Mr. Patrick","Allen, Mr. William Henry","Heikkinen, Miss. Laina"]}
df=pd.DataFrame(data2)
def add_word_count(df):
    df['Word_Count'] = df['text'].str.split().apply(len)
    return df
new_df = add_word_count(df)
print(new_df)