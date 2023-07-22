import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as tick
import numpy as np

def f(x):
    return (75750.02606848886*pow(x+474.0,-1.1825619335627975))


csv =pd.read_csv('LeituraLowPass2.csv')

x=csv['digSignal']
y=csv['distance (cm)']
e=csv['firstFitStd']

fig, ax = plt.subplots(1, 2,figsize=[12.8,5.4])
#ax=plt.gca()

plt.suptitle("Erro e Incerteza")
plt.subplot(121)
plt.title("Erro da curva de ajuste")
plt.xlim(auto=True)
plt.ylim(auto=True)
plt.xlabel("Distância (cm)")
plt.ylabel("Erro (cm)")
plt.plot(y,y-f(x), 'y-',label='Erro')
plt.legend()
ax[0].grid(color='b',alpha=0.2,linestyle='dashed',linewidth=1)



plt.subplot(122)
plt.title("Incerteza")
plt.xlim(auto=True)
plt.ylim(auto=True)
plt.xlabel("Distância (cm)")
plt.ylabel("Incerteza (cm)")
plt.plot(y,2*e/np.sqrt(1000), 'y-',label='Incerteza tipo A')
plt.legend()
ax[1].grid(color='b',alpha=0.2,linestyle='dashed',linewidth=1)

plt.savefig("incertezaSegundaCorrida.png")

