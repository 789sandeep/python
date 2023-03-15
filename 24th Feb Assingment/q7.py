# Q7. You have a Pandas DataFrame df that contains a column named 'Email' that contains email addresses in the format 'username@domain.com'. Write a Python function that creates a new column 'Username' in df that contains only the username part of each email address.z

import pandas as pd

def extract_username(df):
    # Extract username from email addresses
    df['Username'] = df['Email'].apply(lambda x: x.split('@')[0])
    return df
data={"Email":"hello@domain.com"}
df=pd.DataFrame(data)
obj=extract_username(df)
print(obj)