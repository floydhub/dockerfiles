FROM floydhub/dl-base:1.0.0-py2
MAINTAINER Floyd Labs "support@floydhub.com"

# Run Torch7 installation scripts
RUN git clone https://github.com/torch/distro.git /root/torch --recursive \
    && cd /root/torch \
    && bash install-deps \
    && yes no | ./install.sh \
    && cd /root

# Install Jupyter Notebook for iTorch
RUN pip --no-cache-dir install notebook ipywidgets

# Export the LUA evironment variables manually
ENV LUA_PATH='/root/.luarocks/share/lua/5.1/?.lua;/root/.luarocks/share/lua/5.1/?/init.lua;/root/torch/install/share/lua/5.1/?.lua;/root/torch/install/share/lua/5.1/?/init.lua;./?.lua;/root/torch/install/share/luajit-2.1.0-beta1/?.lua;/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua' \
    LUA_CPATH='/root/.luarocks/lib/lua/5.1/?.so;/root/torch/install/lib/lua/5.1/?.so;./?.so;/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so' \
    PATH=/root/torch/install/bin:$PATH \
    LD_LIBRARY_PATH=/root/torch/install/lib:$LD_LIBRARY_PATH \
    DYLD_LIBRARY_PATH=/root/torch/install/lib:$DYLD_LIBRARY_PATH
ENV LUA_CPATH='/root/torch/install/lib/?.so;'$LUA_CPATH

RUN luarocks install nn && \
    luarocks install rnn && \
    luarocks install penlight && \
# Install iTorch
        cd /root && git clone https://github.com/facebook/iTorch.git && \
        cd iTorch && \
        luarocks make