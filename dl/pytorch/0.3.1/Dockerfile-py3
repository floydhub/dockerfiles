FROM floydhub/tensorflow:1.9.0-py3_aws.35
MAINTAINER Floyd Labs "support@floydhub.com"

RUN pip --no-cache-dir install --upgrade \
        http://download.pytorch.org/whl/cpu/torch-0.3.1-cp36-cp36m-linux_x86_64.whl \
        torchvision==0.2.1 \
        torchtext \
        tensorboardX==1.2 \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache