# Q5. How are DataFrame.size() and DataFrame.shape() different?
# In Pandas, DataFrame.size and DataFrame.shape are two methods that are used to get different information about the DataFrame:

# DataFrame.size: returns the total number of elements in the DataFrame, i.e., the product of the number of rows and columns. This method returns a single integer value.

# DataFrame.shape: returns a tuple that contains the number of rows and columns in the DataFrame. The first element of the tuple is the number of rows, and the second element is the number of columns.

# Here's an example to illustrate the difference between these two methods:

import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7,8,9]})

# DataFrame.size
print("Size of DataFrame:", df.size)
# Output: Size of DataFrame: 9

# DataFrame.shape
print("Shape of DataFrame:", df.shape)
# Output: Shape of DataFrame: (3, 3)
# In this example, df.size returns the total number of elements in the DataFrame, which is 9, while df.shape returns a tuple with the number of rows (3) and columns (3) in the DataFrame.