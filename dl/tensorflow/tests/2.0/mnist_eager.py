#@title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Adapted from: 
- https://github.com/tensorflow/docs/blob/master/site/en/guide/eager.ipynb
- https://www.tensorflow.org/guide/eager
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import sys
import time
from tqdm import tqdm


import tensorflow as tf  # pylint: disable=g-bad-import-order
tf.executing_eagerly()

# Log Info
print("-" * 64)
print("TEST INFO - EAGER")
print("-" * 64)
print("TF version:\t {}".format(tf.__version__))
print("Eager execution:\t {}".format(tf.executing_eagerly()))
print("Dataset:\t MNIST")
print("Model:\t CNN")
# GPU?
device_name = tf.test.gpu_device_name()
if device_name == '/device:GPU:0':
    print('Found GPU at:\t {}'.format(device_name))
else:
    print("Found CPU at:\t '[/cpu:0]'")
print("=" * 64)
print("=" * 64)


# Fetch and format the mnist data
(mnist_images, mnist_labels), _ = tf.keras.datasets.mnist.load_data()

dataset = tf.data.Dataset.from_tensor_slices(
  (tf.cast(mnist_images[...,tf.newaxis]/255, tf.float32),
   tf.cast(mnist_labels,tf.int64)))
dataset = dataset.shuffle(1000).batch(32)


# Build the model
mnist_model = tf.keras.Sequential([
  tf.keras.layers.Conv2D(16,[3,3], activation='relu',
                         input_shape=(None, None, 1)),
  tf.keras.layers.Conv2D(16,[3,3], activation='relu'),
  tf.keras.layers.GlobalAveragePooling2D(),
  tf.keras.layers.Dense(10)
])

for images,labels in dataset.take(1):
  print("Logits: ", mnist_model(images[0:1]).numpy())

optimizer = tf.keras.optimizers.Adam()
loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

loss_history = []

def train_step(images, labels):
  with tf.GradientTape() as tape:
    logits = mnist_model(images, training=True)
    
    # Add asserts to check the shape of the output.
    tf.debugging.assert_equal(logits.shape, (32, 10))
    
    loss_value = loss_object(labels, logits)

  loss_history.append(loss_value.numpy().mean())
  grads = tape.gradient(loss_value, mnist_model.trainable_variables)
  optimizer.apply_gradients(zip(grads, mnist_model.trainable_variables))

def train(epochs):
  for epoch in range(epochs):
    for (batch, (images, labels)) in tqdm(enumerate(dataset)):
      train_step(images, labels)
    print ('Epoch {} finished'.format(epoch))
    
train(epochs=1)
