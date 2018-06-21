#!/bin/bash

VERSION=v1

set -e

# buildpack-deps
docker build -t floydhub/buildpack-deps:${VERSION} -f ./base/buildpack-deps/Dockerfile .
docker push floydhub/buildpack-deps:${VERSION}

docker build -t floydhub/buildpack-deps:${VERSION}-gpu -f ./base/buildpack-deps/Dockerfile.gpu .
docker push floydhub/buildpack-deps:${VERSION}-gpu

# dl-deps
floydker build ./base/dl-deps/${VERSION}/Dockerfile-py2
docker push floydhub/dl-deps:${VERSION}-py2

floydker build ./base/dl-deps/${VERSION}/Dockerfile-py3
docker push floydhub/dl-deps:${VERSION}-py3

floydker build ./base/dl-deps/${VERSION}/Dockerfile-py2.gpu
docker push floydhub/dl-deps:${VERSION}-gpu-py2

floydker build ./base/dl-deps/${VERSION}/Dockerfile-py3.gpu
docker push floydhub/dl-deps:${VERSION}-gpu-py3

# dl-python
floydker build ./dl/dl-python/${VERSION}/Dockerfile-py2
docker push floydhub/dl-python:${VERSION}-py2

floydker build ./dl/dl-python/${VERSION}/Dockerfile-py3
docker push floydhub/dl-python:${VERSION}-py3

floydker build ./dl/dl-python/${VERSION}/Dockerfile-py2.gpu
docker push floydhub/dl-python:${VERSION}-gpu-py2

floydker build ./dl/dl-python/${VERSION}/Dockerfile-py3.gpu
docker push floydhub/dl-python:${VERSION}-gpu-py3

# dl-base
floydker build ./dl/dl-base/${VERSION}/Dockerfile-py2
docker push floydhub/dl-base:${VERSION}-py2

floydker build ./dl/dl-base/${VERSION}/Dockerfile-py3
docker push floydhub/dl-base:${VERSION}-py3

floydker build ./dl/dl-base/${VERSION}/Dockerfile-py2.gpu
docker push floydhub/dl-base:${VERSION}-gpu-py2

floydker build ./dl/dl-base/${VERSION}/Dockerfile-py3.gpu
docker push floydhub/dl-base:${VERSION}-gpu-py3
