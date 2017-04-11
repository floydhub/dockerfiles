FROM floydhub/dl-base:latest-py3
MAINTAINER Floyd Labs "support@floydhub.com"

ARG TENSORFLOW_VERSION=0.12.1
ARG TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${TENSORFLOW_VERSION}-cp35-cp35m-linux_x86_64.whl
ARG KERAS_VERSION=1.2.2

RUN pip --no-cache-dir install --upgrade ${TF_BINARY_URL}

# Install Keras
RUN pip --no-cache-dir install git+git://github.com/fchollet/keras.git@${KERAS_VERSION}