# Q5. How are measures of dispersion such as range, variance, and standard deviation used to describe the spread of a dataset? Provide an example.
import numpy as np
class1=[18, 19, 20, 21, 22, 22, 23, 24, 24, 25]
mx=max(class1)
mi=min(class1)
range1=mx-mi
print(range1)
print(np.var(class1))
print(np.std(class1))
