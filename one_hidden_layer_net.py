import numpy as np
from matplotlib import pyplot as plt


def sigmoid(x):
    return 1/(1+np.exp(-x))


# def init_ws(number_of_previous_hidden_layers, number_of_current_hidden_layers):
#     return np.arange(number_of_previous_hidden_layers*number_of_current_hidden_layers)


# def init_bs(number_of_current_hidden_layers):
#     return np.arange(number_of_current_hidden_layers)


# def forward_propagation(ws, a, bs, number_of_previous_hidden_layers, number_of_current_hidden_layers):
#     zs = []
#     a_s = []
#     z = 0
#     for i in range(number_of_current_hidden_layers):
#         w_start_index = i*number_of_previous_hidden_layers
#         for j in range(number_of_previous_hidden_layers):
#             z += a[j]*ws[w_start_index]+bs[i]
#             w_start_index += 1
#         zs.append(z)
#         a_s.append(sigmoid(z))
#     return zs, a_s


m = 100
virulence = np.random.rand(m)
volume = np.random.rand(m)
virulence.sort()
volume.sort()
for i in range(m):
    if virulence[i] < 0.3 or virulence[i] > 0.7:
        virulence[i] = 0
    else:
        virulence[i] = 1

w_1_1_1 = np.random.rand()
w_1_2_1 = np.random.rand()
w_1_1_2 = np.random.rand()
w_2_1_2 = np.random.rand()
b_1_1 = np.random.rand()
b_2_1 = np.random.rand()
b_1_2 = np.random.rand()


def forward_progation(xs):
    z1_1 = w_1_1_1*xs+b_1_1
    a1_1 = sigmoid(z1_1)
    z2_1 = w_1_2_1*xs+b_2_1
    a2_1 = sigmoid(z2_1)
    z1_2 = w_1_1_2*a1_1+b_1_2+w_2_1_2*a2_1+b_1_2
    a1_2 = sigmoid(z1_2)
    return z1_1, a1_1, z2_1, a2_1, z1_2, a1_2


z1_1, a1_1, z2_1, a2_1, z1_2, a1_2 = forward_progation(volume)

alpha = 0.5


def BP(x, y, a1, w2,  a2):
    deda2 = 2*(a2-y)
    da2dz2 = a2*(1-a2)
    dz2dw2 = a1
    dedw2 = deda2*da2dz2*dz2dw2
    dz2db2 = 1
    dedb2 = deda2*da2dz2*dz2db2
    dz2da1 = w2
    da1dz1 = a1*(1-a1)
    dz1dw1 = x
    dedw1 = deda2*da2dz2*dz2da1*da1dz1*dz1dw1
    dz1db1 = 1
    dedb1 = deda2*da2dz2*dz2da1*da1dz1*dz1db1
    return dedw1, dedb1, dedw2, dedw1


for j in range(5500):
    for i in range(m):
        x = volume[i]
        y = virulence[i]
        z1_1, a1_1, z2_1, a2_1, z1_2, a1_2 = forward_progation(x)
        dedw1_1_1, dedb1_1, dedw1_1_2, dedb1_2 = BP(x, y, a1_1, w_1_1_2, a1_2)
        w_1_1_1 = w_1_1_1 - alpha*dedw1_1_1
        w_1_1_2 = w_1_1_2 - alpha*dedw1_1_2
        b_1_1 = b_1_1 - alpha*dedb1_1
        b_1_2 = b_1_2 - alpha*dedb1_2
        dedw1_2_1, dedb2_1, dedw2_1_2, dedb1_2 = BP(x, y, a2_1, w_2_1_2, a1_2)
        w_1_2_1 = w_1_2_1 - alpha*dedw1_2_1
        w_2_1_2 = w_2_1_2 - alpha*dedw2_1_2
        b_2_1 = b_2_1 - alpha*dedb2_1
        b_1_2 = b_1_2 - alpha*dedb1_2

    if j % 100 == 0:
        plt.clf()
        plt.xlabel("volume")
        plt.ylabel("Probability of toxicity")
        plt.scatter(volume, virulence)
        plt.xlim(0, 1.1)
        plt.ylim(0, 1.1)
        z1_1, a1_1, z2_1, a2_1, z1_2, a1_2 = forward_progation(volume)
        plt.plot(volume, a1_2)
        plt.pause(0.01)
plt.show()
