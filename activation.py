import numpy as np
from matplotlib import pyplot as plt

m = 100
virulence = np.random.rand(m)
volume = np.random.rand(m)
virulence.sort()
volume.sort()
for i in range(m):
    if virulence[i] < 0.6:
        virulence[i] = 0
    else:
        virulence[i] = 1
w = 0
b = 0
plt.scatter(volume, virulence)

alpha = 0.5

for j in range(500):
    for i in range(m):
        x = volume[i]
        y = virulence[i]
        z = w*x+b
        a = 1/(1+np.exp(-z))

        deda = 2*(a-y)
        dadz = a*(1-a)
        dzdw = x
        dzdb = 1

        dw = deda*dadz*dzdw
        db = deda*dadz*dzdb

        w = w-alpha*dw
        b = b-alpha*db
    if j % 10 == 0:
        plt.clf()
        plt.xlabel("volume")
        plt.ylabel("Probability of toxicity")
        z = w*volume+b
        a = 1/(1+np.exp(-z))
        plt.scatter(volume, virulence)
        plt.xlim(0, 1.1)
        plt.ylim(0, 1.1)
        plt.plot(volume, a)
        plt.pause(0.01)
print("w: "+str(w))
print("b: "+str(b))
plt.show()
