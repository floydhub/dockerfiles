FROM floydhub/tensorflow:1.9.0-py2_aws.35
MAINTAINER Floyd Labs "support@floydhub.com"

RUN \
    pip --no-cache-dir install \
        mxnet==1.0.0.post4 \
        tensorboardX \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache