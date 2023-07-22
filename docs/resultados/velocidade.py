import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def f(m,x,c):
    return (m*x+c)


csv =pd.read_csv('data (75).csv')
csv=csv[csv['dist']!=0]
x=np.array(csv['tempo'].values,dtype=np.float64)
y=np.array(csv['dist'].values,dtype=np.float64)
xp=[]
yp=[]
for i in csv.index:
    if(i==3):
        print("primeiro")
    else:
        xp.append(csv['tempo'][i]-(x[i]-x[i-1])/2)
        yp.append((y[i]-y[i-1])/(x[i]-x[i-1]))

xp=np.array(xp)
yp=np.array(yp)

fig, ax = plt.subplots(1, 1,figsize=[10.8,10.8])
plt.xlim(auto=True)
plt.ylim(auto=True)

plt.plot(xp,yp)
plt.savefig("buscandoLinearidade.png")