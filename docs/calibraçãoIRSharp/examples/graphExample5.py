import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import numpy as np

fig, ax = plt.subplots(1, figsize=(5,5))

xx = np.linspace(-0.75,1.,100)

ruido = (np.random.rand(len(xx))-0.5)

ax.scatter(xx,xx+0.05*ruido)

plt.legend()
plt.savefig("gauss")