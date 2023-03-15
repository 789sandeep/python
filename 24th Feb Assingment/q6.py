# Q6. Which function of pandas do we use to read an excel file?
# The function in pandas that is used to read an Excel file is read_excel().

# Here's an example code snippet that shows how to use read_excel() to read an Excel file named "example.xlsx" into a pandas DataFrame:
import pandas as pd

# Read Excel file into DataFrame
df = pd.read_excel('file_example_XLS_10.xlsx')

# Do some data manipulation
...

# Display the resulting DataFrame
print(df.head())