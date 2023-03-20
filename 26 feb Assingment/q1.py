# Q1. Is there any difference in the data type of variables list_ and array_list? If there is then write a code to print the data types of both the variables.
import numpy as np
array_list=[1,2,3,4,5]
variable_list=["hello","how","are","you"]
l=np.array(object=array_list)
ls=np.array(object=variable_list)
print(l.dtype)
print(ls.dtype)