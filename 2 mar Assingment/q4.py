# Q4: What is a bar plot? Why is it used? Using the following data plot a bar plot and a horizontal bar plot.
# A bar plot, also known as a bar chart, is a graphical representation of data that uses rectangular bars of equal width to show the relative frequencies or values of different categories. The height of each bar represents the frequency or value of that category, and the bars can be plotted either horizontally or vertically.

# Bar plots are commonly used to display categorical data, such as comparing the frequency of different categories, showing the distribution of data, or comparing data between different groups.

import matplotlib.pyplot as plt
import numpy as np
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])
plt.bar(company,profit)
plt.barh(company,profit)