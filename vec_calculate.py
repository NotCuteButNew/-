import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def sigmoid(z):
    return 1/(1+np.exp(-z))


m = 100
X = np.random.rand(m, 2)
X[X[:, 0].sort()]
Y = np.random.randint(0, 2, m)
Y.sort()
fig = plt.figure()
ax = fig.add_axes(Axes3D(fig))
ax.scatter(X[:, 0], X[:, 1], Y)

W = np.array([0, 0])
B = np.array([0])

alpha = 0.2


def forward_progation(X):
    Z = X.dot(W.T) + B
    return sigmoid(Z)


xs1 = X[:, 0]
xs2 = X[:, 1]
xs1, xs2 = np.meshgrid(xs1, xs2)


for j in range(5000):
    for i in range(m):
        Xi = X[i]
        Yi = Y[i]
        A = forward_progation(Xi)
        E = (Yi-A)**2
        dEdA = 2*(A-Yi)
        dAdZ = A*(1-A)
        dZdW = Xi
        dEdW = dEdA*dAdZ*dZdW
        dZdB = 1
        dEdB = dEdA*dAdZ*dZdB
        W = W - alpha*dEdW
        B = B-alpha*dEdB
    if j % 100 == 0:
        ax.clear()
        ax.scatter(X[:, 0], X[:, 1], Y)
        z = W[0]*xs1 + W[1]*xs2 + B[0]
        a = sigmoid(z)
        ax.plot_surface(xs1, xs2, a, cmap=plt.get_cmap('rainbow'))
        plt.pause(0.1)
plt.show()
