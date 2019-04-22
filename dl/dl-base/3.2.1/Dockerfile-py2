FROM floydhub/dl-python:3.1.0-py2.33
MAINTAINER Floyd Labs "support@floydhub.com"


# Script to install the NodeSource Node.js 8.x LTS Carbon
# repo onto a Debian or Ubuntu system.
RUN wget -qO- https://deb.nodesource.com/setup_8.x | bash -

# Install Nodejs and supervisor for tensorboard and jupyter lab
# lua5.1 and libav-tools for gym retro
# graphviz for visualization
RUN apt-get update && apt-get install -y \
        supervisor \
        binutils \
        nodejs \
        lua5.1 libav-tools \
        nginx \
        graphviz \
        axel \
        imagemagick \
  && apt-get clean \
  && apt-get autoremove \
  && rm -rf /var/cache/apt/archives/* \
  && rm -rf /var/lib/apt/lists/*

COPY tensorboard/tensorboard.conf /etc/supervisor/conf.d/

RUN pip --no-cache-dir install \
        floyd-cli \
        flask==1.0.2 \
        uwsgi==2.0.17 \
        pydot \
        dlib \
        incremental \
        nltk \
        jupyterlab==0.35.4 \
        gym[atari,box2d,classic_control] \
        pattern \
        textacy \
        scikit-image \
        scikit-umfpack \
        spacy \
        tqdm \
        wheel \
        kaggle \
        h5py \
        seaborn \
        plotly \
        annoy \
        pynvrtc \
        menpo \
    && rm -rf /tmp/* /var/tmp/*


# Install and Enable jupyter-widgets
# For JupyterLab 0.35.x, use jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.38
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.38

# Install xgboost
RUN git clone --recursive https://github.com/dmlc/xgboost \
    && cd xgboost \
    && make -j$(nproc) \
    && cd python-package \
    && python setup.py install \
    && cd ../.. \
    && rm -rf xgboost

# Install Anaconda
# RUN wget https://repo.continuum.io/archive/Anaconda3-5.0.0-Linux-x86_64.sh \
#     && bash Anaconda3-5.0.0-Linux-x86_64.sh -b \
#     && rm Anaconda3-5.0.0-Linux-x86_64.sh