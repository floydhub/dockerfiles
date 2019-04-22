FROM floydhub/tensorflow:1.13.0-gpu.cuda9cudnn7-py2_aws.42
MAINTAINER Floyd Labs "support@floydhub.com"

RUN \
    pip --no-cache-dir install \
        mxnet-cu92==1.3.1 \
        tensorboardX \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache