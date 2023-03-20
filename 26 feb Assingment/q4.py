# Q4. Write a code to find the following characteristics of variable, num_array:
# (i) shape
# (ii) size

import numpy as np
num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
num_array = np.array(object = num_list)
print(np.shape(num_array))
print(np.size(num_array))