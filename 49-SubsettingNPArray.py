# NumPy array subsets

import numpy as np

lst1=[1873,46055,2036,92000,58753,24450,29991,2023,48486,45757,20495,22697,87697,54083,12572,9152,28489,3244]
nplist=np.array(lst1)


# Subsetting using index
print(nplist[5])


# subsetting using conditions
print(nplist[nplist>30000])

# Content of Sohamglobal.com