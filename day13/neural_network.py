from tensorflow import *
from keras import *
from keras import layers


input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
output = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

# creating neural network
model = models.Sequential()
# input layer
model.add(layers.Dense(units=5, input_shape=[1]))
# intermediate layer
model.add(layers.Dense(units=200, input_shape=[1]))
model.add(layers.Dense(units=1800, input_shape=[1]))
model.add(layers.Dense(units=320, input_shape=[1]))

model.add(layers.Dense(units=1))

model.compile(optimizer="adam", loss="mean_squared_error")

model.fit(x=input, y=output, epochs=5000)


print(model.predict([13, 14]))
