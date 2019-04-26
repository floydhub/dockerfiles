FROM floydhub/tensorflow:1.13-gpu.cuda9cudnn7-py3_aws.42
MAINTAINER Floyd Labs "support@floydhub.com"

RUN pip --no-cache-dir install --upgrade \
        http://download.pytorch.org/whl/cu90/torch-1.0.1.post2-cp36-cp36m-linux_x86_64.whl \
        torchvision==0.2.1 \
        torchtext \
        tensorboardX==1.2 \
        fastai \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache