import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import numpy as np

def f(x):
    return np.exp(-x*x)


def g(x):
    return np.sin(x)


x=np.linspace(-10,10,1000)
y=np.arange(-10,10,0.01)

fig, ax=plt.subplots(1, figsize=(8,6))

ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')


ax.xaxis.set_major_locator(tick.MultipleLocator(1))
ax.xaxis.set_major_formatter(tick.FormatStrFormatter(r'%g $\pi$'))
ax.xaxis.set_minor_locator(tick.MultipleLocator(0.5))

ax.yaxis.set_major_locator(tick.MultipleLocator(1))
ax.yaxis.set_minor_locator(tick.MultipleLocator(0.5))

plt.setp(ax.xaxis.get_majorticklabels(), rotation=-45,ha="left") 

ax.set_axisbelow(False)
ax.grid(color='b',alpha=0.2,linestyle='dashed',linewidth=1)

#plt.plot(x,f(x), color='cyan',marker='.',label='Gaussiana')

plt.plot(x/np.pi,g(x), 'r-',label=r'$\sin(x)/x$',lw=3)
plt.legend()
plt.savefig("gauss")




