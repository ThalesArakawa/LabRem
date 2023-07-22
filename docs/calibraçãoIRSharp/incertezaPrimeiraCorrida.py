import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as tick
import numpy as np

def f(x):
    return (2536.039588586432*pow(x,-0.7804968904727294))


csv =pd.read_csv('LeituraLowPass2.csv')

x=csv['firstFit']
y=csv['distance (cm)']
e=csv['firstFitStd']

fig, ax = plt.subplots(1, 1,figsize=[10.8,5.4])
#ax=plt.gca()


plt.subplot(111)
plt.title("Erro da curva de ajuste")
plt.xlim(auto=True)
plt.ylim(auto=True)
plt.xlabel("Distância (cm)")
plt.ylabel("Erro (cm)")
plt.plot(y,y-x, 'y-',label='Erro')
plt.legend()
ax.grid(color='b',alpha=0.2,linestyle='dashed',linewidth=1)


plt.savefig("incertezaPrimeiraCorrida.png")

