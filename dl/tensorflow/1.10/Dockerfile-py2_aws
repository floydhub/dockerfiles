FROM floydhub/dl-base:3.1.0-py2.33
MAINTAINER Floyd Labs "support@floydhub.com"

ARG TENSORFLOW_VERSION=v1.10.1
ARG KERAS_VERSION=2.2.2

ENV CI_BUILD_PYTHON python



# install deps for tf build :(
RUN pip --no-cache-dir install \
        funcsigs \
        pbr \
        mock \
        wheel \
        keras_applications \
        keras_preprocessing \
        --no-deps \
    && rm -rf /pip_pkg \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache


# NOTE: This command uses special flags to build an optimized image for AWS machines.
# This image might *NOT* work on other machines
# Clean up pip wheel and Bazel cache when done.
RUN git clone https://github.com/tensorflow/tensorflow.git \
        --branch ${TENSORFLOW_VERSION} \
        --single-branch \
    && cd tensorflow \
    && tensorflow/tools/ci_build/builds/configured CPU \
        bazel build -c opt --copt=-msse3 --copt=-msse4.1 --copt=-msse4.2 \
            --copt=-mavx --copt=-mavx2 \
            --copt=-mfma \
            --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0" \
             \
            --verbose_failures \
            tensorflow/tools/pip_package:build_pip_package \
    && bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/pip \
    && pip --no-cache-dir install --upgrade /tmp/pip/tensorflow-*.whl \
    && rm -rf /pip_pkg \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache \
    && cd .. && rm -rf tensorflow

# Install Keras and tflearn
RUN pip --no-cache-dir install \
        git+git://github.com/fchollet/keras.git@${KERAS_VERSION} \
        tflearn==0.3.2 \
    && rm -rf /pip_pkg \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache