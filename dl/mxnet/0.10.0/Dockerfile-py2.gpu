FROM floydhub/dl-base:1.0.0-gpu-py2
MAINTAINER Floyd Labs "support@floydhub.com"

RUN git clone --branch v0.10.0 --recursive https://github.com/dmlc/mxnet/ && cd mxnet && \
    make -j$(nproc) USE_OPENCV=1 USE_BLAS=openblas USE_CUDA=1 USE_CUDA_PATH=/usr/local/cuda USE_CUDNN=1

ENV PYTHONPATH /mxnet/python