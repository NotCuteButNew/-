import numpy as np
from matplotlib import pyplot as plt

virulence = np.random.rand(100)
volume = np.random.rand(100)
virulence.sort()
volume.sort()

plt.scatter(volume, virulence)

w = 0
alpha = 0.02
for m in range(10):
    for i in range(100):
        x = volume[i]
        y = virulence[i]
        # e = x^2*w^2 + (-2xy)*w + y^2
        # k = 2aw + b
        k = 2*(x**2)*w + (-2*x*y)
        w = w-alpha*k
        plt.clf()
        plt.xlabel("volume")
        plt.ylabel("virulence")
        plt.scatter(volume, virulence)
        plt.xlim(0, 1.1)
        plt.ylim(0, 1.1)
        plt.plot(volume, volume*w)
        plt.pause(0.01)
print("w: "+str(w))
plt.show()
