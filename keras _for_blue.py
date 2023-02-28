
from keras.optimizers import SGD
from keras.layers import Dense
from keras.models import Sequential
import matplotlib.pyplot as plt
import numpy as np


m = 100
y = np.random.rand(m)
x = np.random.rand(m)
y.sort()
x.sort()
for i in range(m):
    if y[i] < 0.5 or y[i] > 0.8:
        y[i] = 0
    else:
        y[i] = 1
w = 0
b = 0
plt.scatter(x, y)

model = Sequential()
dense = Dense(units=2, activation='sigmoid', input_dim=1)
dense2 = Dense(units=1, activation='sigmoid')
model.add(dense)
model.add(dense2)
model.compile(loss='mean_squared_error',
              optimizer=SGD(learning_rate=0.5), metrics=['accuracy'])
model.fit(x, y, epochs=5500, batch_size=10)

pres = model(x)
plt.plot(x, pres)
plt.show()
