FROM floydhub/tensorflow:1.9.0-gpu.cuda9cudnn7-py3_aws.35
MAINTAINER Floyd Labs "support@floydhub.com"

ENV TORCH_CUDA_ARCH_LIST="3.5;5.2;6.0;6.1;6.2;7.0"

RUN pip install \
        typing \
        mkl mkl-devel \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache

RUN export MAX_JOBS=`expr $(nproc) + 1` \
    && git clone https://github.com/pytorch/pytorch \
    && cd pytorch \
    && git checkout v0.4.1 \
    && git submodule update --init \
    && python setup.py install \
    && cd .. && rm -rf pytorch

RUN pip --no-cache-dir install --upgrade \
        torchvision==0.2.1 \
        tensorboardX==1.2 \
        torchtext \
    && rm -rf /tmp/* \
    && rm -rf /root/.cache