import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def f(x):
    return (75750.02606848886*pow(x+474.0,-1.182561933562975))


csv =pd.read_csv('LeituraLowPass2.csv')

x=csv['digSignal']
y=csv['distance (cm)']
e=csv['std']

plt.figure(figsize=[10.8,10.8])
ax=plt.gca()
plt.xlim(auto=True)
plt.ylim(auto=True)

b=np.linspace(470,480,101)
maxr=0
for i in b :
    print(i)
    r=np.corrcoef(np.log10(x+i),np.log10(y))
    r2=r[0][1]*r[1][0]
    if(r2>maxr):
        maxr=r2
        best=i


A = np.vstack([np.log10(x+best), np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, np.log10(y), rcond=None)[0]
r=np.corrcoef(np.log10(x+best),np.log10(y))
r2=r[0][1]*r[1][0]
plt.title("Log-Log")
plt.plot(np.log10(x+best),m*np.log10(x+best)+c, 'r-')
plt.scatter(np.log10(x+best),np.log10(y), s=2)
print(str(pow(10,c))+'*(x +'+str(best)+')^'+str(m))
ax.text(0.1, 0.1, "y = "+str(round(m,4))+"*x + "+str(round(c,4))+'\n'+"r² = "+str(round(r2,4)), horizontalalignment='left', verticalalignment='center', transform=ax.transAxes)
#plt.errorbar(x,y,xerr=e,barsabove=True,ecolor='red',fmt='None')

plt.savefig("regressãoComFator.png")