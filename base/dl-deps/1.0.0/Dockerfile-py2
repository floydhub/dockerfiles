FROM floydhub/python-base:v1-py2
MAINTAINER Floyd Labs "support@floydhub.com"

ENV BAZEL_VERSION 0.16.1

# Add Bazel distribution URI as a package source
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list \
    && curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -

# install older version of bazel because it breaks TF build on every releasae :(
RUN apt-get update && apt-get install -y --no-install-recommends \
        default-jdk-headless \
        bash-completion \
        g++ \
        zlib1g-dev \
    && curl -LO "https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/bazel_${BAZEL_VERSION}-linux-x86_64.deb" \
    && dpkg -i bazel_*.deb \
    && rm bazel_*.deb \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apt/archives/*


# Install some dependencies
RUN apt-get update && apt-get install -y \
        tcl \
        tk \
        ant \
        apt-utils \
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
        libtiff-dev \
        libtiff5-dev \
        libvncserver-dev \
        libzmq3-dev \
        nano \
        net-tools \
        openmpi-bin \
        pkg-config \
        protobuf-compiler \
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


# Install opencv
ARG OPENCV_VERSION=

RUN apt-get update && apt-get install -y \
        libavcodec-dev \
        libavformat-dev \
        libav-tools \
        libavresample-dev \
        libdc1394-22-dev \
        libgdal-dev \
        libgphoto2-dev \
        libgtk2.0-dev \
        libjasper-dev \
        liblapacke-dev \
        libopencore-amrnb-dev \
        libopencore-amrwb-dev \
        libopenexr-dev \
        libswscale-dev \
        libtbb2 \
        libtbb-dev \
        libtheora-dev \
        libv4l-dev \
        libvorbis-dev \
        libvtk6-dev \
        libx264-dev \
        libxine2-dev \
        libxvidcore-dev \
        qt5-default \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apt/archives/*

RUN cd ~/ && \
    git clone https://github.com/Itseez/opencv.git --branch ${OPENCV_VERSION} --single-branch && \
    git clone https://github.com/Itseez/opencv_contrib.git --branch ${OPENCV_VERSION} --single-branch && \
    cd opencv && \
    mkdir build && \
    cd build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
        -DWITH_QT=ON \
        -DWITH_OPENGL=ON \
        -D ENABLE_FAST_MATH=1 \
        -DFORCE_VTK=ON \
        -DWITH_TBB=ON \
        -DWITH_GDAL=ON \
        -DWITH_XINE=ON \
        -DBUILD_EXAMPLES=ON \
        -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
        .. && \
    make -j"$(nproc)" && \
    make install && \
    ldconfig && \
 # Remove the opencv folders to reduce image size
    rm -rf ~/opencv*