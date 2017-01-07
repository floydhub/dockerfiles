FROM floydhub/java-base:8

RUN apt-get install -y \
      unzip \
    && apt-get clean  && \
    rm -rf /var/lib/apt/lists/*

ADD http://nlp.stanford.edu/software/stanford-ner-2015-01-29.zip ner.zip
RUN unzip ner.zip
RUN MV /stanford-ner-2015-01-30 /stanford-ner

WORKDIR /stanford-ner
