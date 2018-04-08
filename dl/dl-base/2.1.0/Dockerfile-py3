FROM floydhub/dl-opencv:3.2.0.1-py3.12
MAINTAINER Floyd Labs "support@floydhub.com"

# Add Tensorboard
RUN apt-get update && apt-get install -y supervisor \
  && apt-get clean \
  && apt-get autoremove \
  && rm -rf /var/cache/apt/archives/* \
  && rm -rf /var/lib/apt/lists/*
COPY tensorboard/tensorboard.conf /etc/supervisor/conf.d/

# graphviz for visualization
RUN apt-get update && apt-get install -y \
        graphviz \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apt/archives/*


RUN pip --no-cache-dir install \
        pydot \
        dlib \
        incremental \
        nltk \
        gym[atari,box2d,classic_control] \
        textacy \
        scikit-image \
        spacy \
        tqdm \
        wheel \
        kaggle-cli \
        annoy \
    && rm -rf /tmp/* /var/tmp/*


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