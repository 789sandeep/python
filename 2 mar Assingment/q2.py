# Q2: What is a scatter plot? Use the following code to generate data for x and y. Using this generated data
# plot a scatter plot.
# import numpy as np
# np.random.seed(3)
# x = 3 + np.random.normal(0, 2, 50)
# y = 3 + np.random.normal(0, 2, len(x))
# Note: Also add title, xlabel, and ylabel to the plot.

# A scatter plot is a graphical representation of a set of data points where each point is represented by its coordinates in a two-dimensional plane. It is used to display the relationship between two variables or to identify patterns in the data. The scatter plot is often used to detect correlations between variables

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))
plt.scatter(x, y)
plt.xlabel("this is x axis")
plt.ylabel("this is y axis")
plt.title("this is plot graph")
plt.show()