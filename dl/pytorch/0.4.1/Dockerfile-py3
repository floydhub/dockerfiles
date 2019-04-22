FROM floydhub/tensorflow:1.13.0-py3_aws.42
MAINTAINER Floyd Labs "support@floydhub.com"

RUN pip --no-cache-dir install --upgrade \
        http://download.pytorch.org/whl/cpu/torch-0.4.1-cp36-cp36m-linux_x86_64.whl \
        torchvision==0.2.1 \
        torchtext \
        tensorboardX==1.2 \
        fastai \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache