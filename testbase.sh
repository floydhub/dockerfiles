#!/bin/bash

VERSION=v1
ARCH=-gpu
PYTHON=-py2

set -euo pipefail

DOCKER_IMAGE=floydhub/dl-base:${VERSION}${ARCH}${PYTHON}

echo "Pulling docker image..."
docker pull ${DOCKER_IMAGE}

echo "Running tests..."
echo "bazel"
docker run ${DOCKER_IMAGE} bazel version
echo "cmake"
docker run ${DOCKER_IMAGE} cmake --version
echo "gfortran"
docker run ${DOCKER_IMAGE} gfortran --version
echo "jupyter"
docker run ${DOCKER_IMAGE} jupyter --version
echo "matplotlib"
docker run ${DOCKER_IMAGE} python -c "import matplotlib"
echo "h5py"
docker run ${DOCKER_IMAGE} python -c "import h5py"
echo "numpy"
docker run ${DOCKER_IMAGE} python -c "import numpy"
echo "pandas"
docker run ${DOCKER_IMAGE} python -c "import pandas"
echo "scipy"
docker run ${DOCKER_IMAGE} python -c "import scipy"
echo "sklearn"
docker run ${DOCKER_IMAGE} python -c "import sklearn"
echo "OpenCV"
docker run ${DOCKER_IMAGE} python -c "import cv2"
echo "gym"
docker run ${DOCKER_IMAGE} python -c "import gym"
echo "nltk"
docker run ${DOCKER_IMAGE} python -c "import nltk"
echo "pattern"
docker run ${DOCKER_IMAGE} python -c "import pattern"
echo "scikit-image"
docker run ${DOCKER_IMAGE} python -c "import skimage"
echo "spacy"
docker run ${DOCKER_IMAGE} python -c "import spacy"
echo "universe"
docker run ${DOCKER_IMAGE} python -c "import universe"
echo "xgboost"
docker run ${DOCKER_IMAGE} python -c "import xgboost"