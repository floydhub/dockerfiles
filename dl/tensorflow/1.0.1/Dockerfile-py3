FROM floydhub/dl-base:1.0.0-py3.6
MAINTAINER Floyd Labs "support@floydhub.com"

ARG TENSORFLOW_VERSION=1.0.1
ARG TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${TENSORFLOW_VERSION}-cp35-cp35m-linux_x86_64.whl
ARG KERAS_VERSION=2.0.6

RUN pip --no-cache-dir install --upgrade ${TF_BINARY_URL}

# Add Tensorboard
RUN apt-get update && apt-get install -y supervisor \
  && apt-get clean \
  && apt-get autoremove \
  && rm -rf /var/cache/apt/archives/* \
  && rm -rf /var/lib/apt/lists/*
COPY tensorboard/tensorboard.conf /etc/supervisor/conf.d/

# Install Keras and tflearn
RUN pip --no-cache-dir install git+git://github.com/fchollet/keras.git@${KERAS_VERSION} \
        tflearn==0.3.2 \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache