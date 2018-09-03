# Multi dimensional arrays

import numpy as np

n=np.array([[9,13,26],[16,8,1]])

print("Data Type : ",n.dtype)
print("Type : ",type(n))
print("Dimensions : ",n.shape)

# prints row of index 1
print(n[1,:])

#prints columns of index 1 of all rows
print(n[:,1])

# Content of Sohamglobal.com