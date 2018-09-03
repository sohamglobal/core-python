import matplotlib.pyplot as plt

x1=57
x2=35
x3=20
x4=45
x5=65
col=["red","green","orange","blue"]
lab=["5th Sem","3rd Sem","7th Sem","4th Sem"]
plt.pie([x1,x2,x3,x4],colors=col,labels=lab)
plt.legend(title="Semesters")
plt.axis("equal")
plt.show()
# Content of SohamGlobal.com