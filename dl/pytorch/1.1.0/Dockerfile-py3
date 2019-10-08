FROM floydhub/tensorflow:1.14-py3_aws.44
MAINTAINER Floyd Labs "support@floydhub.com"

RUN pip --no-cache-dir install --upgrade \
        http://download.pytorch.org/whl/cpu/torch-1.1.0-cp36-cp36m-linux_x86_64.whl \
        # Torchvision is now built with CUDA https://github.com/pytorch/vision/issues/946 
        https://download.pytorch.org/whl/cpu/torchvision-0.3.0-cp36-cp36m-linux_x86_64.whl \
        torchtext==0.4.0 \
        tensorboardX==1.8 \
        fastai \
        transformers \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache