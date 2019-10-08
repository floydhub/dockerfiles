FROM floydhub/tensorflow:1.14-gpu.cuda10cudnn7-py3_aws.46
MAINTAINER Floyd Labs "support@floydhub.com"

RUN pip --no-cache-dir install --upgrade \
        http://download.pytorch.org/whl/cu100/torch-1.1.0-cp36-cp36m-linux_x86_64.whl \
        http://download.pytorch.org/whl/cu100/torchvision-1.1.0-cp36-cp36m-linux_x86_64.whl \
        torchtext==0.4.0 \
        tensorboardX==1.8 \
        fastai \
        transformers \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache