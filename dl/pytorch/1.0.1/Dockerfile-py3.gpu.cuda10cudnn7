FROM floydhub/tensorflow:1.13-gpu.cuda10cudnn7-py3_aws.46
MAINTAINER Floyd Labs "support@floydhub.com"

RUN pip --no-cache-dir install --upgrade \
        http://download.pytorch.org/whl/cu100/torch-1.0.1.post2-cp36-cp36m-linux_x86_64.whl \
        http://download.pytorch.org/whl/cu100/torchvision-1.0.1.post2-cp36-cp36m-linux_x86_64.whl \
        torchtext== \
        tensorboardX==1.2 \
        fastai \
        transformers \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache