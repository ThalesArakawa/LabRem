import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.exp(-x*x)


def g(x):
    return np.sin(x)



x=np.linspace(-10,10,1000)
y=np.arange(-10,10,0.01)

plt.figure(figsize=(10,10))
#plt.xlim(auto=True)
#plt.ylim(auto=True)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("TestGraficos")

ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.xaxis.set_label_coords(1.02,0.5)
ax.tick_params(which='major',length=5,width=2)
yt=np.arange(-1,1.01,0.5)
plt.yticks(yt)
xt=np.arange(-2,2.1,1)
xl=[r'$-2\pi$',r'$-\pi$','',r'$\pi$',r'$2\pi$']
plt.xticks(xt,xl)
ax.set_xticks(xt)
ax.set_xticklabels(xl,fontsize=16)
ax.set_axisbelow(False)
ax.grid(color='b',alpha=0.2,linestyle='dashed',linewidth=1)

plt.plot(x,f(x), color='cyan',marker='.',label='Gaussiana')
plt.plot(x/np.pi,g(x), 'r-',label=r'$\sin(x)/x$',lw=3)
plt.legend()
plt.savefig("gauss")




