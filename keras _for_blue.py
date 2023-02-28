import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

m = 100
y = np.random.rand(m)
x = np.random.rand(m)
y.sort()
x.sort()
for i in range(m):
    if y[i] < 0.6:
        y[i] = 0
    else:
        y[i] = 1
w = 0
b = 0
plt.scatter(x, y)

model = Sequential()
dense = Dense(units=1, activation='sigmoid', input_dim=1)
model.add(dense)

model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])
model.fit(x, y, epochs=5000, batch_size=10)

pres = model(x)
plt.plot(x, pres)
plt.show()
