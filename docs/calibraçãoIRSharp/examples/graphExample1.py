import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.exp(-x*x)


def g(x):
    return np.sin(x)/x



x=np.linspace(-10,10,1000)
y=np.arange(-10,10,0.01)

plt.figure(figsize=[10,10], facecolor='y',frameon=True)
plt.xlim(auto=True)
plt.ylim(auto=True)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("TestGraficos")

ax=plt.gca()
ax.spines['right'].set_color('red')
ax.spines['top'].set_color('red')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
#ax.set_aspect(1)

plt.plot(x,f(x), color='cyan',marker='.',label='Gaussiana')
plt.plot(x,g(x), 'r-',label=r'$\sin(x)/x$')
plt.legend()
plt.savefig("gauss")




