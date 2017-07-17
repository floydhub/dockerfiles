FROM floydhub/dl-base:1.0.0-py2
MAINTAINER Floyd Labs "support@floydhub.com"

RUN git clone --branch v0.10.0 --recursive https://github.com/dmlc/mxnet/ && cd mxnet && \
    make -j$(nproc) USE_OPENCV=1 USE_BLAS=openblas 

ENV PYTHONPATH /mxnet/python