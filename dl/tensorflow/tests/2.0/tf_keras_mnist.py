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
'''
Adapted from:
- https://www.tensorflow.org/tutorials/quickstart/beginner
- https://github.com/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb
'''

from __future__ import print_function
import sys
import time

import tensorflow as tf

# Log Info
print("-" * 64)
print("TEST INFO - SESSION")
print("-" * 64)
print("TF version:\t {}".format(tf.__version__))
print("Dataset:\t MNIST")
print("Model:\t CNN")

# GPU?
device_name = tf.test.gpu_device_name()
if device_name == '/device:GPU:0':
    print('Found GPU at:\t {}'.format(device_name))
else:
    print("Found CPU at:\t '[/cpu:0]'")
print("=" * 64)

# Parameters
learning_rate = 0.001
training_iters = 200000
batch_size = 128
display_step = 10

# Load and scale the data
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# 2 Layer NN
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)
