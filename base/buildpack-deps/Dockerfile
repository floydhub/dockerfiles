FROM buildpack-deps:bionic
MAINTAINER FloydHub "support@floydhub.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
		sudo \
	&& rm -rf /var/lib/apt/lists/*
