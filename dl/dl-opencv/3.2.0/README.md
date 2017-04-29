The GPU versions of OpenCV timeout when building on Docker Hub. They have to be built locally and pushed to the Docker Registry.

To build Docker image locally (Note: takes a few hours):
* Python 2: `docker build -t floydhub/dl-opencv:3.2.0-gpu-py2 -f Dockerfile-py2.gpu .`
* Python 3: `docker build -t floydhub/dl-opencv:3.2.0-gpu-py3 -f Dockerfile-py3.gpu .`

To push image to Docker registry:
* Python 2: `docker push floydhub/dl-opencv:3.2.0-gpu-py2`
* Python 3: `docker push floydhub/dl-opencv:3.2.0-gpu-py3`