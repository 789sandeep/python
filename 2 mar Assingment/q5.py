# Q5: What is a box plot? Why is it used? Using the following data plot a box plot.
# A box plot, also known as a box-and-whisker plot, is a graphical representation of the distribution of a dataset. It shows the median, quartiles, and outliers of the data. The box in the plot represents the interquartile range (IQR), which is the range between the first quartile (Q1) and third quartile (Q3). The whiskers extend from the box and show the range of the data, excluding any outliers.

# Box plots are useful for comparing the distribution of data between different groups or datasets. They can help identify differences in central tendency, spread, and skewness between the groups

import numpy as np
import matplotlib.pyplot as plt

# Create two datasets
box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)

# Combine the datasets into a list
data = [box1, box2]
plt.boxplot(data)
plt.show()
