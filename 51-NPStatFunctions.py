# NumPy functions

import numpy as np

nplst=np.array([1,2,3,4,5,6,7,8,9,10])

print(nplst)

print("Sum : ",np.sum(nplst))
print("Average : ",np.average(nplst))
print("Mean : ",np.mean(nplst))

# the value separating the higher half of a data sample from the lower half
print("Median : ",np.median(nplst))

# The Pearson product-moment correlation coefficients
print("Corelation Coefficient : ",np.corrcoef(nplst))

# the square root of the average of squared deviations from mean
print("Standard Deviation : ",np.std(nplst))


# the minimum and the maximum from the elements in the given array
print("Amin : ",np.amin(nplst))
print("Amax : ",np.amax(nplst))

# the value below which a given percentage of observations in a group of observations fall
print("Percentile : ",np.percentile(nplst,20))


# Variance is the average of squared deviations, i.e., mean(abs(x - x.mean())**2)
print("Variance : ",np.var(nplst))

# Content of Sohamglobal.com


