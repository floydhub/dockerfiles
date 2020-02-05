FROM floydhub/tensorflow:2.0-py3_aws.54
MAINTAINER Floyd Labs "support@floydhub.com"

RUN pip --no-cache-dir install --upgrade \
        https://download.pytorch.org/whl/cpu/torch-1.2.0%2Bcpu-cp36-cp36m-manylinux1_x86_64.whl \
        # Torchvision is now built with CUDA https://github.com/pytorch/vision/issues/946 
        https://download.pytorch.org/whl/cpu/torchvision-0.4.0%2Bcpu-cp36-cp36m-manylinux1_x86_64.whl \
        torchtext==0.4.0 \
        tensorboardX==1.9 \
        fastai \
        transformers \
	tokenizers \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache

# Fix Jupyterlab - see https://github.com/jupyter/jupyter/issues/401
# TODO: move this on dl-base
RUN pip --no-cache-dir install --upgrade notebook \
    && rm -rf /pip_pkg \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache
