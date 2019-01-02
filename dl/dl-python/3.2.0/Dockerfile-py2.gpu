FROM floydhub/dl-deps:3.2.0-gpu.39
MAINTAINER Floyd Labs "support@floydhub.com"

RUN  apt-get update \
    && apt-get install -y --no-install-recommends \
        python-pip \
        python-setuptools \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apt/archives/*

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
        ipykernel==4.9.0 \
        ipython==5.6.0 \
        matplotlib==2.2.3 \
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
COPY jupyter_notebook_config_py2.py /root/.jupyter/
RUN mv /root/.jupyter/jupyter_notebook_config_py2.py /root/.jupyter/jupyter_notebook_config.py

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