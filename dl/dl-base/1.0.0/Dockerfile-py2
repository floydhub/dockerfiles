FROM floydhub/dl-opencv:3.2.0-py2.6
MAINTAINER Floyd Labs "support@floydhub.com"

RUN pip --no-cache-dir install \
        dlib \
        gym[all] \
        incremental \
        nltk \
        pattern \
        textacy \
        scikit-image \
        spacy \
        tqdm \
        wheel

# Install OpenAI Universe
RUN git clone --branch v0.21.3 https://github.com/openai/universe.git \
    && cd universe \
    && pip install . \
    && cd .. \
    && rm -rf universe

# Install xgboost
RUN git clone --recursive https://github.com/dmlc/xgboost \
    && cd xgboost \
    && make -j$(nproc) \
    && cd python-package \
    && python setup.py install \
    && cd ../.. \
    && rm -rf xgboost