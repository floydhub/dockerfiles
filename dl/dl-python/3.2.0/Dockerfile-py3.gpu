FROM floydhub/dl-deps:3.2.0-gpu.39
MAINTAINER Floyd Labs "support@floydhub.com"

# From https://github.com/docker-library/python/blob/master/3.6./Dockerfile

# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

ENV GPG_KEY 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D
ENV PYTHON_VERSION 3.6.5

RUN set -ex \
	&& apt-get update \
		&& apt-get install -y --no-install-recommends \
			dpkg-dev \
			tcl-dev \
			tk-dev \
		&& apt-get clean \
		&& apt-get autoremove \
		&& rm -rf /var/lib/apt/lists/* \
		&& rm -rf /var/cache/apt/archives/* \
	\
	&& wget -O python.tar.xz "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz" \
	&& wget -O python.tar.xz.asc "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \
	&& gpg --batch --verify python.tar.xz.asc python.tar.xz \
	&& rm -r "$GNUPGHOME" python.tar.xz.asc \
	&& mkdir -p /usr/src/python \
	&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \
	&& rm python.tar.xz \
	\
	&& cd /usr/src/python \
	&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
	&& ./configure \
		--build="$gnuArch" \
		--with-tcltk-includes='-I/usr/include/tk -I/usr/include/tcl' \
		--with-tcltk-libs='/usr/lib/x86_64-linux-gnu/libtcl.so /usr/lib/x86_64-linux-gnu/libtk.so' \
		--enable-loadable-sqlite-extensions \
		--enable-shared \
		--with-system-expat \
		--with-system-ffi \
		--without-ensurepip \
	&& make -j$(nproc) \
	&& make install \
	&& ldconfig \
	&& find /usr/local -depth \
		\( \
			\( -type d -a -name test -o -name tests \) \
			-o \
			\( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
		\) -exec rm -rf '{}' + \
	&& rm -rf /usr/src/python ~/.cache

# make some useful symlinks that are expected to exist
RUN cd /usr/local/bin \
	&& { [ -e easy_install ] || ln -s easy_install-* easy_install; } \
	&& ln -s idle3 idle \
	&& ln -s pydoc3 pydoc \
	&& ln -s python3 python \
	&& ln -s python3-config python-config


# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid truth value '<VERSION>'"
ENV PYTHON_PIP_VERSION 10.0.1

RUN set -ex; \
    \
    wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'; \
    \
    python get-pip.py \
        --disable-pip-version-check \
        --no-cache-dir \
        "pip==$PYTHON_PIP_VERSION" \
    ; \
    pip --version; \
    \
    find /usr/local -depth \
        \( \
            \( -type d -a \( -name test -o -name tests \) \) \
            -o \
            \( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
        \) -exec rm -rf '{}' +; \
    rm -f get-pip.py

RUN pip --no-cache-dir install \
        virtualenv \
        PyOpenGL PyOpenGL_accelerate \
        Cython \
        h5py \
        jupyter \
        notebook==5.6.0 \
        numpy \
        cupy \
        pandas \
        matplotlib \
        ipykernel \
        path.py \
        pyyaml \
        scipy \
        six \
        sklearn \
        sympy \
        Pillow \
        zmq \
        opencv-contrib-python==3.4.0.12 \
    && rm -rf /tmp/* /var/tmp/* \
    && python -m ipykernel.kernelspec

# Set up our notebook config.
COPY jupyter_notebook_config_py3.py /root/.jupyter/
RUN mv /root/.jupyter/jupyter_notebook_config_py3.py /root/.jupyter/jupyter_notebook_config.py

# Create the file configurations for IPython
# and remove the default one.
RUN ipython profile create && rm /root/.ipython/profile_default/ipython_config.py

# Set up our IPython config.
COPY ipython_config.py /root/.ipython/profile_default/ipython_config.py

# Jupyter has issues with being run directly:
#   https://github.com/ipython/ipython/issues/7062
# We just add a little wrapper script.
COPY run_jupyter.sh /
RUN chmod +x /run_jupyter.sh

# IPython
EXPOSE 8888

CMD ["/run_jupyter.sh"]