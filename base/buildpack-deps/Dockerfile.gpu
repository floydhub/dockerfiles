FROM nvidia/cuda:9.2-cudnn7-devel-ubuntu16.04
MAINTAINER FloydHub "support@floydhub.com"

ENV LIBRARY_PATH=/usr/local/cuda/lib64/stubs:$LIBRARY_PATH
ENV LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        sudo \
        # Based on https://github.com/docker-library/buildpack-deps/tree/master/xenial
        ca-certificates \
        curl \
        wget \
        # build related deps
        bzr \
        git \
        mercurial \
        openssh-client \
        subversion \
        # procps is very common in build systems, and is a reasonably small package
        procps \
        autoconf \
        automake \
        bzip2 \
        file \
        g++ \
        gcc \
        imagemagick \
        libbz2-dev \
        libc6-dev \
        libcurl4-openssl-dev \
        libdb-dev \
        libevent-dev \
        libffi-dev \
        libgdbm-dev \
        libgeoip-dev \
        libglib2.0-dev \
        libjpeg-dev \
        libkrb5-dev \
        liblzma-dev \
        libmagickcore-dev \
        libmagickwand-dev \
        libncurses-dev \
        libpng-dev \
        libpq-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        libtool \
        libwebp-dev \
        libxml2-dev \
        libxslt-dev \
        libyaml-dev \
        make \
        patch \
        xz-utils \
        zlib1g-dev \
        # https://lists.debian.org/debian-devel-announce/2016/09/msg00000.html
        $( \
        # if we use just "apt-cache show" here, it returns zero because "Can't select versions from package 'libmysqlclient-dev' as it is purely virtual", hence the pipe to grep
            if apt-cache show 'default-libmysqlclient-dev' 2>/dev/null | grep -q '^Version:'; then \
            echo 'default-libmysqlclient-dev'; \
            else \
            echo 'libmysqlclient-dev'; \
            fi \
        ) \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apt/archives/*

# setup libnccl links for tensorflow build
# see: https://github.com/tensorflow/tensorflow/commit/1fda7645d132b71b9084b01945795e97e582adcd#diff-ade1d3e4b7c35655f854151d899df62bR1134
RUN cd /usr/local/cuda-* \
    && ln -sf lib64 lib \
    && ln -sf /usr/lib/x86_64-linux-gnu/libnccl.so ./lib/libnccl.so.2 \
    && ln -sf /usr/include/nccl.h ./include/nccl.h

# This updates the global environment for the root user
RUN echo "LIBRARY_PATH=/usr/local/cuda/lib64/stubs:$LIBRARY_PATH" >> /etc/environment
RUN echo "LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH" >> /etc/environment
