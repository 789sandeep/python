# Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
# you give an example of when you might use one of these functions?

# There are many built-in functions in Pandas that you can use to manipulate data in a DataFrame. Here are some common ones:

# head(): This function returns the first n rows of a DataFrame. This is useful when you want to quickly check the structure of your data or get a sense of what the data looks like.

# tail(): This function returns the last n rows of a DataFrame. This is useful when you want to check the end of your data or see if there are any patterns or trends over time.

# describe(): This function provides a summary of the statistical properties of each column in a DataFrame, including the count, mean, standard deviation, minimum, maximum, and quartiles. This is useful for getting a quick understanding of the distribution of the data.

# sort_values(): This function sorts the rows of a DataFrame by one or more columns. This is useful when you want to sort your data by a particular variable or look for patterns in the data.

# groupby(): This function groups the rows of a DataFrame by one or more columns and then applies a function (such as mean, median, sum, etc.) to each group. This is useful when you want to aggregate your data by category or find relationships between variables.

# fillna(): This function replaces missing values in a DataFrame with a specified value or method (such as forward filling or backward filling). This is useful when you want to clean your data and ensure that missing values do not affect your analysis.
import pandas as pd

# create a DataFrame with customer information
data = {'age': [25, 30, 35, 40, 25, 30, 35, 40],
        'gender': ['M', 'M', 'F', 'F', 'M', 'M', 'F', 'F'],
        'spending': [100, 200, 150, 300, 75, 250, 175, 350]}
df = pd.DataFrame(data)

# group the data by age and gender and calculate the mean spending for each group
grouped = df.groupby(['age', 'gender']).mean()

# print the result
print(grouped)