import numpy as np
from matplotlib import pyplot as plt

m = 100
virulence = np.random.rand(m)
volume = np.random.rand(m)
virulence.sort()
volume.sort()

plt.subplot(1, 2, 1)
plt.xlabel("volume")
plt.ylabel("virulence")
plt.scatter(volume, virulence)
w_min = np.sum(volume*virulence)/np.sum(volume**2)
print("w_win: "+str(w_min))
plt.plot(volume, volume*w_min)

plt.subplot(1, 2, 2)
plt.xlabel("w")
plt.ylabel("e")

ws = np.arange(0, 2, 0.01)
es = []
for w in ws:
    predition = w*volume
    e = np.sum((predition-virulence)**2)*(1/m)
    es.append(e)
plt.plot(ws, es)

plt.show()
