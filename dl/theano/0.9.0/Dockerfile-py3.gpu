FROM floydhub/dl-base:1.0.0-gpu-py3
MAINTAINER Floyd Labs "support@floydhub.com"

ARG THEANO_VERSION=rel-0.9.0
ARG LASAGNE_VERSION=e71bc59b509d2c0cf67622b0d94c69f51b588bd4
ARG KERAS_VERSION=2.0.3

# Install Theano and set up Theano config (.theanorc) for CUDA and OpenBLAS
RUN pip --no-cache-dir install git+git://github.com/Theano/Theano.git@${THEANO_VERSION} \
    \
    && echo "[global]\
        \ndevice=cuda\
        \nfloatX=float32\
        \noptimizer_including=cudnn\nmode=FAST_RUN\
        \n[gpuarray]\npreallocate=0.95\
        \n[nvcc]\
        \nfastmath=True\
        \n[blas]\
        \nldflag=-L/usr/lib/openblas-base -lopenblas\
        \n[DebugMode]\
        \ncheck_finite=1"\
    > /root/.theanorc \
    && rm -rf /tmp/* /var/tmp/*

RUN git clone --branch v0.6.5 https://github.com/Theano/libgpuarray.git \
    && cd libgpuarray \
    && cmake . -DCMAKE_BUILD_TYPE=Release \
    && make -j$(nproc) \
    && make install \
    && ldconfig \
    && python setup.py build \
    && python setup.py install \
    && cd .. && rm -rf libgpuarray

# Install Lasagne
RUN pip --no-cache-dir install --upgrade --no-deps \
    git+git://github.com/Lasagne/Lasagne.git@${LASAGNE_VERSION} \
    && rm -rf /tmp/* /var/tmp/*

# Install Keras
RUN pip --no-cache-dir install git+git://github.com/fchollet/keras.git@${KERAS_VERSION} \
    && rm -rf /tmp/* /var/tmp/*

# Set Backed to Theano
ENV KERAS_BACKEND='theano'