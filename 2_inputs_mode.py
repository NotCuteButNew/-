import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def sigmoid(z):
    return 1/(1+np.exp(-z))


m = 100
xs = np.random.rand(m, 2)
xs[xs[:, 0].sort()]
ys = np.random.randint(0, 2, m)
ys.sort()
fig = plt.figure()
ax = fig.add_axes(Axes3D(fig))
ax.scatter(xs[:, 0], xs[:, 1], ys)

w1 = 0
w2 = 0
b = 0

alpha = 0.2


def forward_progation(x1, x2):
    z = w1*x1 + w2*x2 + b
    return sigmoid(z)


xs1 = xs[:, 0]
xs2 = xs[:, 1]
xs1, xs2 = np.meshgrid(xs1, xs2)


for j in range(500):
    for i in range(m):
        x1 = xs[i, 0]
        x2 = xs[i, 1]
        y = ys[i]
        a = forward_progation(x1, x2)
        deda = 2*(a-y)
        dadz = a*(1-a)
        dzdw1 = x1
        dzdw2 = x2
        dedw1 = deda*dadz*dzdw1
        dedw2 = deda*dadz*dzdw2
        dzdb = 1
        dedb = deda*dadz*dzdb
        w1 = w1-alpha*dedw1
        w2 = w2-alpha*dedw2
        b = b-alpha*dedb
    if j % 100 == 0:
        ax.clear()
        ax.scatter(xs[:, 0], xs[:, 1], ys)
        a = forward_progation(xs1, xs2)
        ax.plot_surface(xs1, xs2, a, cmap=plt.get_cmap('rainbow'))
        plt.pause(0.1)
plt.show()
