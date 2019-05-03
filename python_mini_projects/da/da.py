import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sdata = pd.read_csv("da.csv")
print(sdata)

name = sdata.NAME.tolist()
sem1 = sdata.SEM1.tolist()
sem2 = sdata.SEM2.tolist()

print(name)
print(sem1)
print(sem2)

x = np.arange(len(name))
plt.bar(x,sem1,width=0.25,label='SEM1')
plt.bar(x+0.25,sem2,width=0.25,label='SEM2')
plt.xticks(x,name)

plt.xlabel("NAMES")
plt.ylabel("MARKS")
plt.legend()
plt.show()