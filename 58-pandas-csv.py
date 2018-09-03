import pandas as pd

data=pd.read_csv("Sales.csv")

print(type(data))

# Dimensions of dataframe
print(data.shape)

# Select first 5 rows
print(data.head(5))

# Select last 2 rows
print(data.tail(2))

# fetch columns
print(data.columns)

print("Index Info : ",data.index)

print("DataFrame Info \n-----------------------")
print(data.info())

