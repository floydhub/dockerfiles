#! /bin/bash
#############################
#   TF 1.4 Testing Script   #
#############################

# TF Session
python mnist_session.py

# TF Estimator
python mnist_estimator.py

# Keras Test
python keras_mnist_test.py

# Delete benchmarks folder if exists
if test -d benchmarks; then
	rm -rf benchmarks
fi

# Clone Benchmarks and go to a certain commit
git clone https://github.com/tensorflow/benchmarks.git && cd benchmarks
git reset --hard d967962 # POSSIBLE PARAMETER
cd scripts/tf_cnn_benchmarks

sed -i '/import interleave_ops/d' preprocessing.py

# Check if GPU is installed (quick hack)
which nvidia-smi &> /dev/null
ISGPU=$?

if test $ISGPU -eq 1; then
	# CPU or CPU2?
	NCORE=`cat /proc/cpuinfo | grep processor | wc -l`

	# Quick Benchmark on AlexNet (syntethic images, no data transformation, channel last)
	if test $NCORE -eq 2; then
		# CPU test (defined initial lr otherwise Loss is NaN )
		python tf_cnn_benchmarks.py --device=cpu  --kmp_blocktime=0 --nodistortions --model=alexnet --data_format=NHWC --batch_size=32  --num_inter_threads=1 --num_intra_threads=$NCORE --learning_rate=0.00001
	else
		# CPU2 test
		python tf_cnn_benchmarks.py --device=cpu  --kmp_blocktime=0 --nodistortions --model=alexnet --data_format=NHWC --batch_size=64  --num_inter_threads=1 --num_intra_threads=$NCORE --learning_rate=0.00001
	fi
else
	# GPU or GPU2?
	nvidia-smi | grep -q V100
	ISV100=$?

	# Quick Benchmark on Resnet-50 (syntethic images, no data transformation, channel first)
	if test $ISV100 -eq 1; then
		# GPU test
		python tf_cnn_benchmarks.py --device=gpu --num_gpus=1 --batch_size=64 --model=resnet50 --nodistortions --data_format=NCHW
	else
		# GPU2 test (with MXP)
		python tf_cnn_benchmarks.py --device=gpu --num_gpus=1 --batch_size=256 --model=resnet50 --nodistortions --data_format=NCHW --use_fp16=true --use_tf_layers=false
	fi
fi

