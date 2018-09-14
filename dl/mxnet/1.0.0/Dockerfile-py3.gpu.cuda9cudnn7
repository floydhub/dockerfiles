FROM floydhub/tensorflow:1.9.0-gpu.cuda9cudnn7-py3_aws.35
MAINTAINER Floyd Labs "support@floydhub.com"

RUN \
    pip --no-cache-dir install \
        mxnet-cu91==1.0.0.post4 \
        tensorboardX \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache