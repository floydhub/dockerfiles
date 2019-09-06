FROM floydhub/tensorflow:1.14-gpu.cuda9cudnn7-py3_aws.44
MAINTAINER Floyd Labs "support@floydhub.com"

RUN pip --no-cache-dir install --upgrade \
        http://download.pytorch.org/whl/cu90/torch-1.1.0-cp36-cp36m-linux_x86_64.whl \
        torchvision==0.3.0 \
        torchtext==0.4.0 \
        tensorboardX==1.8 \
        fastai \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache