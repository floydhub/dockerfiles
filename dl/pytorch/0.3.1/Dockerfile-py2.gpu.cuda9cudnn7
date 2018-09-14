FROM floydhub/tensorflow:1.9.0-gpu.cuda9cudnn7-py2_aws.35
MAINTAINER Floyd Labs "support@floydhub.com"

RUN pip --no-cache-dir install --upgrade \
        http://download.pytorch.org/whl/cu91/torch-0.3.1-cp27-cp27mu-linux_x86_64.whl \
        torchvision==0.2.1 \
        torchtext \
        tensorboardX==1.2 \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache