FROM floydhub/dl-base:2.1.0-gpu-py3.13
MAINTAINER Floyd Labs "support@floydhub.com"

ARG TENSORFLOW_VERSION=v1.4.0
ARG KERAS_VERSION=2.0.8

RUN git clone https://github.com/tensorflow/tensorflow.git --branch ${TENSORFLOW_VERSION} --single-branch
WORKDIR /tensorflow

ENV CI_BUILD_PYTHON python
# Configure the build for our CUDA configuration.
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
ENV TF_CUDA_VERSION 8.0
ENV TF_CUDNN_VERSION 6
ENV TF_NEED_CUDA 1
ENV TF_CUDA_COMPUTE_CAPABILITIES=3.7,7.0



# NOTE: This command uses special flags to build an optimized image for AWS machines.
# This image might *NOT* work on other machines
# Clean up pip wheel and Bazel cache when done.
RUN tensorflow/tools/ci_build/builds/configured GPU \
    && bazel build -c opt --copt=-msse3 --copt=-msse4.1 --copt=-msse4.2 --copt=-mavx --copt=-mavx2 \
        --copt=-mfma \
        --config=monolithic \
        --config=cuda tensorflow/tools/pip_package:build_pip_package \
    && bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/pip \
    && pip --no-cache-dir install --upgrade /tmp/pip/tensorflow-*.whl \
    && rm -rf /pip_pkg \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache \
    && cd / && rm -rf tensorflow

# Add Tensorboard
RUN apt-get update && apt-get install -y supervisor \
  && apt-get clean \
  && apt-get autoremove \
  && rm -rf /var/cache/apt/archives/* \
  && rm -rf /var/lib/apt/lists/*
COPY tensorboard/tensorboard.conf /etc/supervisor/conf.d/

WORKDIR /

# Install Keras and tflearn
RUN pip --no-cache-dir install git+git://github.com/fchollet/keras.git@${KERAS_VERSION} \
        tflearn==0.3.2 \
    && rm -rf /pip_pkg \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache