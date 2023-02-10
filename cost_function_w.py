import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

m = 100
virulence = np.random.rand(m)
volume = np.random.rand(m)
virulence.sort()
volume.sort()

plt.scatter(volume, virulence)
plt.xlabel("volume")
plt.ylabel("virulence")

ws = np.arange(0, 2, 0.01)
bs = np.arange(0, 2, 0.01)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_zlim(0, 0.5)

for b in bs:
    es = []
    for w in ws:
        predition = w*volume + b
        e = np.sum((predition-virulence)**2)*(1/m)
        es.append(e)
    ax.plot(ws, es, b, zdir='y')
plt.show()
