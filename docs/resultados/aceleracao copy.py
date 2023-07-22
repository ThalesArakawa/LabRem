import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
datas={74,75,77,78,79}

csv=pd.read_csv('data (83).csv')
csv=csv[csv['dist']!=0]
poly=np.polyfit(csv['tempo'].values,csv['dist'].values,2)
r2=1
sq=0
st=0
ybar=np.average(csv['dist'].values)
for i in csv.index:
    sq=sq+(csv['dist'][i]-poly[0]*csv['tempo'][i]**2-poly[1]*csv['tempo'][i]-poly[2])**2
    st=st+(csv['dist'][i]-ybar)**2


r2=1-sq/st

fig, ax = plt.subplots(1, 1,figsize=[10.8,10.8])
plt.subplot(111)
plt.title("Curva de ajuste")
plt.xlabel("Tempo (ms)")
plt.ylabel("Distância (cm)")
plt.xlim(auto=True)
plt.ylim(0,20)
x=np.linspace(0,3000,3000)
plt.plot(x,poly[0]*x**2+poly[1]*x+poly[2],'r-',label='Valores do Ajuste')
plt.scatter(csv['tempo'].values,csv['dist'].values,label='Valores Coletados')
ax.text(0.1, 0.9,"y = "+str(round(poly[0],8))+'x² '+str(round(poly[1],8))+'x '+str(round(poly[2],8))+'\n'+ "r² = "+str(round(r2,4)), horizontalalignment='left', verticalalignment='center', transform=ax.transAxes)

plt.savefig("ajustePolinomial.png")
