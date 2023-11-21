import tensorflow as tf
import numpy as np
from tensorflow.python.keras  import Sequential
from tensorflow.python.keras.layers import Dense

#create a class to use to check if when training that accuracy is 95%
# it checks if the epoch log is above .95
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('accuracy')>0.95):
            print("\nReached 95% accuracy so cancelling training!")
            self.model.stop_training = True
callbacks = myCallback()


#This imports the fashion Mnist database, its a database of about 60,000 images in 28x28pix grayscale
#keras has many different datasets you can practice on
data = tf.keras.datasets.fashion_mnist

#uses the load_data method to load them for us as tuples
(training_images, training_labels), (test_images, test_lables) = data.load_data()

#data smoothing by dividing all images by 255 so their grayscale is either 1 or 0
training_images = training_images/255.0
test_images = test_images/255.0

#activations are what type of operation the nerons are using
#relu is rectified linear unit, it returns a value if its greater than 0
#softmax simply gives us which has the largest value
#128 neurons was chosen arbitrarily, but this will need to be tweaked on other networks
#more neurons = more time, but more accuracy
#10 was chosen for the last layer since we have 10 possible answers
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

#this loss model is good for picking categories
model.compile(
    optimizer='adam',
    loss="sparse_categorical_crossentropy",
    metrics=(['accuracy'])
)

#compare training_images to training labels 5 times
model.fit(training_images, training_labels, epochs=50, callbacks=[callbacks])

model.evaluate(test_images, test_lables)

#allows the network to guess what the first image in the set is
classifications = model.predict(test_images)
print(classifications[0])
print(test_lables[0])