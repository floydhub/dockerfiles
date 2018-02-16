FROM floydhub/dl-base:1.0.0-py2.6
MAINTAINER Floyd Labs "support@floydhub.com"

RUN pip --no-cache-dir install --upgrade http://download.pytorch.org/whl/cu80/torch-0.1.12.post1-cp27-none-linux_x86_64.whl \
    tensorboardX
# install torch vision from source for dataloader bug fix
# ref: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/issues/63
RUN git clone https://github.com/pytorch/vision \
    && cd vision \
    && git checkout 7492fae4c2cd16fb2783dce7e7583d7245cfbe92 \
    && python setup.py install \
    && cd .. \
    && rm -rf vision
