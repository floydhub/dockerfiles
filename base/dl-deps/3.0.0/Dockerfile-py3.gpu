FROM floydhub/python-base:3.0.0-gpu-py3
MAINTAINER Floyd Labs "support@floydhub.com"

# Add Bazel distribution URI as a package source
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list \
    && curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -

# Install some dependencies
RUN apt-get update && apt-get install -y \
        ant \
        apt-utils \
        bazel \
        bc \
        build-essential \
        cmake \
        default-jdk \
        doxygen \
        gfortran \
        golang \
        iptables \
        libav-tools \
        libboost-all-dev \
        libeigen3-dev \
        libfreetype6-dev \
        libhdf5-dev \
        libjpeg-turbo8-dev \
        liblcms2-dev \
        libopenblas-dev \
        liblapack-dev \
        libpng12-dev \
        libprotobuf-dev \
        libsdl2-dev \
        libpython3-dev \
        libtiff-dev \
        libtiff5-dev \
        libvncserver-dev \
        libzmq3-dev \
        nano \
        net-tools \
        openmpi-bin \
        pkg-config \
        protobuf-compiler \
        python3-dev \
        python3-opengl \
        python3-tk \
        python-software-properties \
        rsync \
        software-properties-common \
        swig \
        unzip \
        vim \
        webp \
        xorg-dev \
        xvfb \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apt/archives/* \
# Link BLAS library to use OpenBLAS using the alternatives mechanism (https://www.scipy.org/scipylib/building/linux.html#debian-ubuntu)
    && update-alternatives --set libblas.so.3 /usr/lib/openblas-base/libblas.so.3

# Install Git LFS
RUN apt-get update \
    && add-apt-repository ppa:git-core/ppa \
    && curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && \
    apt-get install -y git-lfs \
    && git lfs install \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/cache/apt/archives/* \
    && rm -rf /var/lib/apt/lists/*