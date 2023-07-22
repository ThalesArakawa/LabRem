import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def f(m,x,c):
    return (m*x+c)


csv =pd.read_csv('LeituraLowPass2.csv')

x=csv['digSignal']
y=csv['distance (cm)']
e=csv['std']

fig, ax = plt.subplots(2, 2,figsize=[10.8,10.8])
plt.xlim(auto=True)
plt.ylim(auto=True)


A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
r=np.corrcoef(x,y)
r2=r[0][1]*r[1][0]
plt.subplot(221)
plt.title("Lin-Lin")
plt.plot(x,m*x+c, 'r-')
plt.scatter(x,y, s=2)
ax[0][0].text(0.1, 0.1, "y = "+str(round(m,4))+"*x + "+str(round(c,4))+'\n'+"r² = "+str(round(r2,4)), horizontalalignment='left', verticalalignment='center', transform=ax[0][0].transAxes)
#plt.errorbar(x,y,xerr=e,barsabove=True,ecolor='red',fmt='None')

A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, np.log10(y), rcond=None)[0]
r=np.corrcoef(x,np.log10(y))
r2=r[0][1]*r[1][0]
plt.subplot(222)
plt.title("Log-Lin")
plt.plot(x,m*x+c, 'r-')
plt.scatter(x,np.log10(y), s=2)
ax[0][1].text(1.3, 0.1, "y = "+str(round(m,4))+"*x + "+str(round(c,4))+'\n'+"r² = "+str(round(r2,4)), horizontalalignment='left', verticalalignment='center', transform=ax[0][0].transAxes)
#plt.errorbar(x,np.log10(y),xerr=e,barsabove=True,ecolor='red',fmt='None')

A = np.vstack([np.log10(x), np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
r=np.corrcoef(np.log10(x),y)
r2=r[0][1]*r[1][0]
plt.subplot(223)
plt.title("Lin-Log")
plt.plot(np.log10(x),m*np.log10(x)+c, 'r-')
plt.scatter(np.log10(x),y, s=2)
ax[1][0].text(0.1, -1.1, "y = "+str(round(m,4))+"*x + "+str(round(c,4))+'\n'+"r² = "+str(round(r2,4)), horizontalalignment='left', verticalalignment='center', transform=ax[0][0].transAxes)
#plt.errorbar(np.log10(x),y,xerr=np.log10(e),barsabove=True,ecolor='red',fmt='None')

A = np.vstack([np.log10(x), np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, np.log10(y), rcond=None)[0]
r=np.corrcoef(np.log10(x),np.log10(y))
r2=r[0][1]*r[1][0]
plt.subplot(224)
plt.title("Log-Log")
plt.plot(np.log10(x),m*np.log10(x)+c, 'r-')
plt.scatter(np.log10(x),np.log10(y), s=2)
ax[1][1].text(1.3, -1.1, "y = "+str(round(m,4))+"*x + "+str(round(c,4))+'\n'+"r² = "+str(round(r2,4)), horizontalalignment='left', verticalalignment='center', transform=ax[0][0].transAxes)
#plt.errorbar(x,y,xerr=e,barsabove=True,ecolor='red',fmt='None')

fig.suptitle(' Linearização ', fontsize=30)

plt.savefig("buscandoLinearidade.png")