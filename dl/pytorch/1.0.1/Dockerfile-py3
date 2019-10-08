FROM floydhub/tensorflow:1.13-py3_aws.42
MAINTAINER Floyd Labs "support@floydhub.com"

RUN pip --no-cache-dir install --upgrade \
        http://download.pytorch.org/whl/cpu/torch-1.0.1.post2-cp36-cp36m-linux_x86_64.whl \
        # Torchvision is now built with CUDA https://github.com/pytorch/vision/issues/946 
        https://download.pytorch.org/whl/cpu/torchvision-0.2.1-cp36-cp36m-linux_x86_64.whl \
        torchtext== \
        tensorboardX==1.2 \
        fastai \
        transformers \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache