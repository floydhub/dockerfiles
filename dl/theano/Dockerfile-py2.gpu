FROM floydhub/dl-base:latest-gpu-py2
MAINTAINER Floyd Labs "support@floydhub.com"

ARG THEANO_VERSION=rel-0.8.2
ARG LASAGNE_VERSION=v0.1
ARG KERAS_VERSION=1.2.2

# Install Theano and set up Theano config (.theanorc) for CUDA and OpenBLAS
RUN pip --no-cache-dir install git+git://github.com/Theano/Theano.git@${THEANO_VERSION} && \
	\
	echo "[global]\ndevice=gpu\nfloatX=float32\noptimizer_including=cudnn\nmode=FAST_RUN \
		\n[lib]\ncnmem=0.95 \
		\n[nvcc]\nfastmath=True \
		\n[blas]\nldflag = -L/usr/lib/openblas-base -lopenblas \
		\n[DebugMode]\ncheck_finite=1" \
	> /root/.theanorc

# Install Lasagne
RUN pip --no-cache-dir install git+git://github.com/Lasagne/Lasagne.git@${LASAGNE_VERSION}

# Install Keras
RUN pip --no-cache-dir install git+git://github.com/fchollet/keras.git@${KERAS_VERSION}

# Set Backed to Theano
ENV KERAS_BACKEND='theano'