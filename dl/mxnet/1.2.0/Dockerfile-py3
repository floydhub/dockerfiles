FROM floydhub/tensorflow:1.9.0-py3_aws.35
MAINTAINER Floyd Labs "support@floydhub.com"

RUN \
    pip --no-cache-dir install \
        mxnet==1.2.0 \
        tensorboardX \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache