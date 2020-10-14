FROM floydhub/tensorflow:2.3-gpu.cuda10cudnn7-py3_aws.56
MAINTAINER Floyd Labs "support@floydhub.com"

RUN pip --no-cache-dir install --upgrade \
        http://download.pytorch.org/whl/cu102/torch-1.6.0-cp37-cp37m-linux_x86_64.whl \
        http://download.pytorch.org/whl/cu102/torchvision-0.7.0-cp37-cp37m-linux_x86_64.whl \
        torchtext==0.7.0 \
        tensorboardX==2.1 \
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