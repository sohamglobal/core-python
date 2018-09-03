import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("Mydata.csv")
data=data.head(20)
x=data["SrNo"]
y=data["Sem"]

plt.bar(x,y,color=["green","blue","yellow"],label="Registration Data")

plt.title("Roll_No Vs Semester Graph",color="limegreen")
# plt.legend()

plt.show()