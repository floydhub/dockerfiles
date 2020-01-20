FROM buildpack-deps:bionic

RUN apt-get update && apt-get install -y --no-install-recommends \
		sudo \
	&& rm -rf /var/lib/apt/lists/*
