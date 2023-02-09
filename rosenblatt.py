import numpy as np
from matplotlib import pyplot as plt

virulence = np.random.rand(100)
volume = np.random.rand(100)
virulence.sort()
volume.sort()

plt.scatter(volume, virulence)

w = 0
alpha = 0.05

for m in range(10000):
    for i in range(100):
        x = volume[i]
        y = virulence[i]
        predition = y * w
        error = y-predition
        w = w + alpha * error * x

plt.plot(volume, volume*w)
plt.show()
