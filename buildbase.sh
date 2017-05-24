#!/bin/bash

VERSION=v1

set -e

# buildpack-deps
docker build -t floydhub/buildpack-deps:${VERSION} -f ./base/buildpack-deps/Dockerfile .
docker push floydhub/buildpack-deps:${VERSION}

docker build -t floydhub/buildpack-deps:${VERSION}-gpu -f ./base/buildpack-deps/Dockerfile.gpu .
docker push floydhub/buildpack-deps:${VERSION}-gpu

# python-base
sed -i "1s/:latest/:${VERSION}/g" ./base/python-base/2.7/Dockerfile
docker build -t floydhub/python-base:${VERSION}-py2 -f ./base/python-base/2.7/Dockerfile .
docker push floydhub/python-base:${VERSION}-py2
sed -i "1s/:${VERSION}/:latest/g" ./base/python-base/2.7/Dockerfile

sed -i "1s/:latest/:${VERSION}/g" ./base/python-base/3.5/Dockerfile
docker build -t floydhub/python-base:${VERSION}-py3 -f ./base/python-base/3.5/Dockerfile .
docker push floydhub/python-base:${VERSION}-py3
sed -i "1s/:${VERSION}/:latest/g" ./base/python-base/3.5/Dockerfile

sed -i "1s/:latest/:${VERSION}/g" ./base/python-base/2.7/Dockerfile.gpu
docker build -t floydhub/python-base:${VERSION}-gpu-py2 -f ./base/python-base/2.7/Dockerfile.gpu .
docker push floydhub/python-base:${VERSION}-gpu-py2
sed -i "1s/:${VERSION}/:latest/g" ./base/python-base/2.7/Dockerfile.gpu

sed -i "1s/:latest/:${VERSION}/g" ./base/python-base/3.5/Dockerfile.gpu
docker build -t floydhub/python-base:${VERSION}-gpu-py3 -f ./base/python-base/3.5/Dockerfile.gpu .
docker push floydhub/python-base:${VERSION}-gpu-py3
sed -i "1s/:${VERSION}/:latest/g" ./base/python-base/3.5/Dockerfile.gpu

# dl-deps
sed -i "1s/:latest/:${VERSION}/g" ./base/dl-deps/Dockerfile-py2
docker build -t floydhub/dl-deps:${VERSION}-py2 -f ./base/dl-deps/Dockerfile-py2 .
docker push floydhub/dl-deps:${VERSION}-py2
sed -i "1s/:${VERSION}/:latest/g" ./base/dl-deps/Dockerfile-py2

sed -i "1s/:latest/:${VERSION}/g" ./base/dl-deps/Dockerfile-py3
docker build -t floydhub/dl-deps:${VERSION}-py3 -f ./base/dl-deps/Dockerfile-py3 .
docker push floydhub/dl-deps:${VERSION}-py3
sed -i "1s/:${VERSION}/:latest/g" ./base/dl-deps/Dockerfile-py3

sed -i "1s/:latest/:${VERSION}/g" ./base/dl-deps/Dockerfile-py2.gpu
docker build -t floydhub/dl-deps:${VERSION}-gpu-py2 -f ./base/dl-deps/Dockerfile-py2.gpu .
docker push floydhub/dl-deps:${VERSION}-gpu-py2
sed -i "1s/:${VERSION}/:latest/g" ./base/dl-deps/Dockerfile-py2.gpu

sed -i "1s/:latest/:${VERSION}/g" ./base/dl-deps/Dockerfile-py3.gpu
docker build -t floydhub/dl-deps:${VERSION}-gpu-py3 -f ./base/dl-deps/Dockerfile-py3.gpu .
docker push floydhub/dl-deps:${VERSION}-gpu-py3
sed -i "1s/:${VERSION}/:latest/g" ./base/dl-deps/Dockerfile-py3.gpu

# dl-python
sed -i "1s/:latest/:${VERSION}/g" ./dl/dl-python/Dockerfile-py2
docker build -t floydhub/dl-python:${VERSION}-py2 -f ./dl/dl-python/Dockerfile-py2 ./dl/dl-python
docker push floydhub/dl-python:${VERSION}-py2
sed -i "1s/:${VERSION}/:latest/g" ./dl/dl-python/Dockerfile-py2

sed -i "1s/:latest/:${VERSION}/g" ./dl/dl-python/Dockerfile-py3
docker build -t floydhub/dl-python:${VERSION}-py3 -f ./dl/dl-python/Dockerfile-py3 ./dl/dl-python
docker push floydhub/dl-python:${VERSION}-py3
sed -i "1s/:${VERSION}/:latest/g" ./dl/dl-python/Dockerfile-py3

sed -i "1s/:latest/:${VERSION}/g" ./dl/dl-python/Dockerfile-py2.gpu
docker build -t floydhub/dl-python:${VERSION}-gpu-py2 -f ./dl/dl-python/Dockerfile-py2.gpu ./dl/dl-python
docker push floydhub/dl-python:${VERSION}-gpu-py2
sed -i "1s/:${VERSION}/:latest/g" ./dl/dl-python/Dockerfile-py2.gpu

sed -i "1s/:latest/:${VERSION}/g" ./dl/dl-python/Dockerfile-py3.gpu
docker build -t floydhub/dl-python:${VERSION}-gpu-py3 -f ./dl/dl-python/Dockerfile-py3.gpu ./dl/dl-python
docker push floydhub/dl-python:${VERSION}-gpu-py3
sed -i "1s/:${VERSION}/:latest/g" ./dl/dl-python/Dockerfile-py3.gpu

# dl-opencv
sed -i "1s/:latest/:${VERSION}/g" ./dl/dl-opencv/3.2.0/Dockerfile-py2
docker build -t floydhub/dl-opencv:${VERSION}-py2 -f ./dl/dl-opencv/3.2.0/Dockerfile-py2 ./dl/dl-opencv/3.2.0
docker push floydhub/dl-opencv:${VERSION}-py2
sed -i "1s/:${VERSION}/:latest/g" ./dl/dl-opencv/3.2.0/Dockerfile-py2

sed -i "1s/:latest/:${VERSION}/g" ./dl/dl-opencv/3.2.0/Dockerfile-py3
docker build -t floydhub/dl-opencv:${VERSION}-py3 -f ./dl/dl-opencv/3.2.0/Dockerfile-py3 ./dl/dl-opencv/3.2.0
docker push floydhub/dl-opencv:${VERSION}-py3
sed -i "1s/:${VERSION}/:latest/g" ./dl/dl-opencv/3.2.0/Dockerfile-py3

sed -i "1s/:latest/:${VERSION}/g" ./dl/dl-opencv/3.2.0/Dockerfile-py2.gpu
docker build -t floydhub/dl-opencv:${VERSION}-gpu-py2 -f ./dl/dl-opencv/3.2.0/Dockerfile-py2.gpu ./dl/dl-opencv/3.2.0
docker push floydhub/dl-opencv:${VERSION}-gpu-py2
sed -i "1s/:${VERSION}/:latest/g" ./dl/dl-opencv/3.2.0/Dockerfile-py2.gpu

sed -i "1s/:latest/:${VERSION}/g" ./dl/dl-opencv/3.2.0/Dockerfile-py3.gpu
docker build -t floydhub/dl-opencv:${VERSION}-gpu-py3 -f ./dl/dl-opencv/3.2.0/Dockerfile-py3.gpu ./dl/dl-opencv/3.2.0
docker push floydhub/dl-opencv:${VERSION}-gpu-py3
sed -i "1s/:${VERSION}/:latest/g" ./dl/dl-opencv/3.2.0/Dockerfile-py3.gpu

# dl-base
sed -i "1s/:latest/:${VERSION}/g" ./dl/dl-base/Dockerfile-py2
docker build -t floydhub/dl-base:${VERSION}-py2 -f ./dl/dl-base/Dockerfile-py2 ./dl/dl-base
docker push floydhub/dl-base:${VERSION}-py2
sed -i "1s/:${VERSION}/:latest/g" ./dl/dl-base/Dockerfile-py2

sed -i "1s/:latest/:${VERSION}/g" ./dl/dl-base/Dockerfile-py3
docker build -t floydhub/dl-base:${VERSION}-py3 -f ./dl/dl-base/Dockerfile-py3 ./dl/dl-base
docker push floydhub/dl-base:${VERSION}-py3
sed -i "1s/:${VERSION}/:latest/g" ./dl/dl-base/Dockerfile-py3

sed -i "1s/:latest/:${VERSION}/g" ./dl/dl-base/Dockerfile-py2.gpu
docker build -t floydhub/dl-base:${VERSION}-gpu-py2 -f ./dl/dl-base/Dockerfile-py2.gpu ./dl/dl-base
docker push floydhub/dl-base:${VERSION}-gpu-py2
sed -i "1s/:${VERSION}/:latest/g" ./dl/dl-base/Dockerfile-py2.gpu

sed -i "1s/:latest/:${VERSION}/g" ./dl/dl-base/Dockerfile-py3.gpu
docker build -t floydhub/dl-base:${VERSION}-gpu-py3 -f ./dl/dl-base/Dockerfile-py3.gpu ./dl/dl-base
docker push floydhub/dl-base:${VERSION}-gpu-py3
sed -i "1s/:${VERSION}/:latest/g" ./dl/dl-base/Dockerfile-py3.gpu