#! /bin/bash
#############################
#   TF 2.0 Testing Script   #
#############################

# TF Session
python tf_keras_mnist.py

# TF Eager
python mnist_eager.py

# Keras Test
python keras_mnist_test.py


# Consider to move from tf.tf_cnn_benchmarks to perfzero https://github.com/tensorflow/benchmarks/tree/master/perfzero