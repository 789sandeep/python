# Q3. Considering the following changes in the variable, array_list:
# array_list = np.array(object = list_, dtype = int)
# Will there be any difference in the data type of the elements present in both the variables, list_ and arra_list? If so then print the data types of each and every element present in both the variables, list_ and arra_list.

import numpy as np
list_=[1,2,3,4,5]
for i in list_:
    print(type(i))
array_list=np.array(object=list_,dtype=int)
for i in array_list:
    print(i.dtype)