# Torch

A basic image with [Torch](http://torch.ch/) installed. Contains minimal additional packages.

The GPU versions of Torch timeout when building on Docker Hub. They have to be built locally and pushed to the Docker Registry.

To build Docker image locally (Note: takes a few hours):
* Python 2: `docker build -t floydhub/torch:latest-gpu-py2 -f Dockerfile-py2.gpu .`
* Python 3: `docker build -t floydhub/torch:latest-gpu-py3 -f Dockerfile-py3.gpu .`

To push image to Docker registry:
* Python 2: `docker push floydhub/torch:latest-gpu-py2`
* Python 3: `docker push floydhub/torch:latest-gpu-py3`