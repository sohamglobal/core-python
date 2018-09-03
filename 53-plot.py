import matplotlib.pyplot as plt

year=[1930,1950,1970,1990,2010]
pop=[3.231,1.519,4.692,2.263,6.972]

# plt.xlabel("Year")
# plt.ylabel("Polulation")

# plt.title("Yearwise Polulation Data")

plt.xlim(1920,2050)
plt.ylim(0,7.5)

#plt.grid(True)

plt.plot(year,pop)
plt.show()

# Content of Sohamglobal.com