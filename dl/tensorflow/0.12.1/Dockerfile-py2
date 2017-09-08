FROM floydhub/dl-base:1.0.0-py2.6
MAINTAINER Floyd Labs "support@floydhub.com"

ARG TENSORFLOW_VERSION=0.12.1
ARG TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${TENSORFLOW_VERSION}-cp27-none-linux_x86_64.whl
ARG KERAS_VERSION=1.2.2

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