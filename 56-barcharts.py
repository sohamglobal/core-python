import matplotlib.pyplot as plt

year=[1930,1940,1950,1960,1970]
pop=[50000,67000,52000,80000,70000]

color=["red","orange","pink","green","blue"]

plt.xlabel("Year")
plt.ylabel("Polulation")

plt.title("Yearwise Polulation Data")

#plt.barh(year,pop,height=6,color=color)
plt.bar(year,pop,width=8,color=color)

plt.show()

# Content of SohamGlobal.com

