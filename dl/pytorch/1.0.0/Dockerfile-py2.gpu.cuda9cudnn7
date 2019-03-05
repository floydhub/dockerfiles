FROM floydhub/tensorflow:1.13.0-gpu.cuda9cudnn7-py2_aws.41
MAINTAINER Floyd Labs "support@floydhub.com"

RUN pip --no-cache-dir install --upgrade \
        http://download.pytorch.org/whl/cu90/torch-1.0.0-cp27-cp27mu-linux_x86_64.whl \
        torchvision==0.2.1 \
        torchtext \
        tensorboardX==1.2 \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache