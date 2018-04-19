# Imports
import numpy as np
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)

def main(unused_argv):
	# Log Info
	print("-" * 64)
	print("TEST INFO - ESTIMATOR")
	print("-" * 64)
	print("TF version:\t {}".format(tf.__version__))
	print("Dataset:\t MNIST")
	print("Model:\t pre-made estimator DNNClassifier")

	# GPU?
	device_name = tf.test.gpu_device_name()
	if device_name == '/device:GPU:0':
		print('Found GPU at:\t {}'.format(device_name))
	else:
		print("Found CPU at:\t '[/cpu:0]'")
	print("=" * 64)

	# Load training and eval data
	mnist = tf.contrib.learn.datasets.load_dataset("mnist")

	train_data = mnist.train.images # Returns np.array
	train_labels = np.asarray(mnist.train.labels, dtype=np.int32)
	eval_data = mnist.test.images # Returns np.array
	eval_labels = np.asarray(mnist.test.labels, dtype=np.int32)

	# Define the features and the pre-made estimator model
	feature_columns = [tf.feature_column.numeric_column("x", shape=[28, 28])]

	estimator = tf.estimator.DNNClassifier(
					 feature_columns=feature_columns,
					 hidden_units=[512,],
					 activation_fn=tf.nn.relu,
					 optimizer='RMSProp',
					 n_classes=10)

	# Train input pipeline
	train_input_fn = tf.estimator.inputs.numpy_input_fn(
		x={"x": train_data},
		y=train_labels,
		batch_size=100,
		num_epochs=1,
		shuffle=True)

	# Eval input pipeline
	eval_input_fn = tf.estimator.inputs.numpy_input_fn(
	    x={"x": eval_data},
	    y=eval_labels,
	    num_epochs=1,
	    shuffle=False)

	train_spec = tf.estimator.TrainSpec(input_fn=train_input_fn, max_steps=3000)
	eval_spec = tf.estimator.EvalSpec(input_fn=eval_input_fn)

	# Train and Evaluate
	tf.estimator.train_and_evaluate(estimator, train_spec, eval_spec)


if __name__ == "__main__":
  tf.app.run()