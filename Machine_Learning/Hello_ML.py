import tensorflow as tf
import numpy as np
from tensorflow.python.keras  import Sequential
from tensorflow.python.keras.layers import Dense

#let model know the numbers are in a sequence
model = tf.keras.Sequential()
#add a layer, the layer is dense, all points are connected, of 1 with 1 neuron.
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))
#compiler information
model.compile(optimizer='sgd', loss='mean_squared_error')

#input data
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

#running the model, comparing xs to ys 500 times
model.fit(xs, ys, epochs=500)

#predeict y for when x == 10, then print to consolew
print(model.predict([10.0]))