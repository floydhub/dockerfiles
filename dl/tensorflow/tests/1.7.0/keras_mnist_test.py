import keras
import tensorflow as tf
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical

# Log Info
print("-" * 64)
print("TEST INFO - KERAS")
print("-" * 64)
print("TF version:\t {}".format(tf.__version__))
print("Keras Version:\t {}".format(keras.__version__))
print("Dataset:\t MNIST")
print("Model:\t Sequential-DNN")

# GPU?
device_name = tf.test.gpu_device_name()
if device_name == '/device:GPU:0':
	print('Found GPU at:\t {}'.format(device_name))
else:
	print("Found CPU at:\t '[/cpu:0]'")

print("=" * 64)


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print("Train shape:", train_images.shape)
print("Train samples:", len(train_labels))
print("Train labels:", train_labels)

print("Test shape:", test_images.shape)
print("Test samples:", len(test_labels))
print("Test labels:", test_labels)

# Build the Model
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# Pre-processing (Reshaping and normalization)
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# One hot encoding for labels
# e.g. labels 5 => [0,0,0,0,1,...,0]
train_labels = to_categorical(train_labels)
print("Train labels (one-hot-encoding):", train_labels)
test_labels = to_categorical(test_labels)
print("Test labels (one-hot-encoding):", test_labels)

# Training
network.fit(train_images, train_labels, epochs=5, batch_size=100)

# Eval
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc:', test_acc)
