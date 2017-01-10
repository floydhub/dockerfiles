FROM floydhub/torch-gpu:latest
MAINTAINER Floyd Labs "support@floydhub.com"

RUN luarocks install tds && \
	luarocks install nngraph && \
	luarocks install bit32

# Install OpenNMT
RUN git clone https://github.com/opennmt/opennmt.git && \
		cd opennmt && \
		luarocks make rocks/opennmt-scm-1.rockspec

WORKDIR "/opennmt"
