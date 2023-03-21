# Q3: Why is the subplot() function used? Draw four line plots using the subplot() function.
# Use the following data:
# import numpy as np
# For line 1: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([0, 100, 200, 300, 400, 500])
# For line 2: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([50, 20, 40, 20, 60, 70])
# For line 3: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([10, 20, 30, 40, 50, 60])
# For line 4: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([200, 350, 250, 550, 450, 150])

# The subplot() function is used to create multiple plots in a single figure. It takes three arguments: the number of rows, the number of columns, and the index of the current plot. It allows for easy comparison of multiple datasets or multiple representations of a single dataset.


import matplotlib.pyplot as plt
import numpy as np

# Data for line 1
x1 = np.array([0, 1, 2, 3, 4, 5])
y1 = np.array([0, 100, 200, 300, 400, 500])

# Data for line 2
x2 = np.array([0, 1, 2, 3, 4, 5])
y2 = np.array([50, 20, 40, 20, 60, 70])

# Data for line 3
x3 = np.array([0, 1, 2, 3, 4, 5])
y3 = np.array([10, 20, 30, 40, 50, 60])

# Data for line 4
x4 = np.array([0, 1, 2, 3, 4, 5])
y4 = np.array([200, 350, 250, 550, 450, 150])

fig=plt.figure(figsize=(9,1))
# Create a 2x2 subplot grid
fig, axs = plt.subplots(2,2)

# Plot line 1 in the top-left subplot
axs[0, 0].plot(x1, y1)
axs[0, 0].set_title('Line 1')

# Plot line 2 in the top-right subplot
axs[0, 1].plot(x2, y2)
axs[0, 1].set_title('Line 2')

# Plot line 3 in the bottom-left subplot
axs[1, 0].plot(x3, y3)
axs[1, 0].set_title('Line 3')

# Plot line 4 in the bottom-right subplot
axs[1, 1].plot(x4, y4)
axs[1, 1].set_title('Line 4')

# Add a main title to the figure
fig.suptitle('Four Line Plots')

# Show the figure
plt.show()

