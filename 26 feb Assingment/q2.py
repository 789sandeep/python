# Q2. Write a code to print the data type of each and every element of both the variables list_ and arra_list.

import numpy as np
l=[[1,2,3],[4,5,8],[6,7,8]]
lv=[["heelo"],["how"],["are"],["you"]]
array_list=np.array(object=l)
for i in array_list:
    print(i.dtype)
variable_list=np.array(object=lv) 
for i in variable_list:
    print(i.dtype)  