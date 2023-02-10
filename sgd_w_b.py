import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

m = 100
virulence = np.random.rand(m)+0.5
volume = np.random.rand(m)
virulence.sort()
volume.sort()

plt.scatter(volume, virulence)

w = 0
b = 0
alpha = 0.5


for j in range(500):
    for i in range(m):
        x = volume[i]
        y = virulence[i]
        dw = 2*(x**2)*w+2*x*b+(-2*x*y)
        db = 2*b+2*x*w - 2*y
        w = w-alpha*dw
        b = b-alpha*db
    plt.clf()
    plt.xlabel("volume")
    plt.ylabel("virulence")
    plt.scatter(volume, virulence)
    plt.xlim(0, 1.1)
    plt.ylim(0, 1.6)
    plt.plot(volume, volume*w+b)
    plt.pause(0.01)
print("w: "+str(w))
print("b: "+str(b))
plt.show()
