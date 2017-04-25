## Warning
The Tensorflow 1.0 images are built from source and use optimization flags for best performance on AWS machines. 
This might or might not work on your machine (e.g. you might see an `Illegal Instruction` error). 
Use with caution!

Building from source will timeout on Docker Hub. They have to be built locally and pushed to the Docker Registry.

To build Docker image locally (Note: takes a few hours):
* Python 2: `docker build -t floydhub/tensorflow:1.0-py2 -f Dockerfile-py2 .`
* Python 2 GPU: `docker build -t floydhub/tensorflow:1.0-gpu-py2 -f Dockerfile-py2.gpu .`
* Python 3: `docker build -t floydhub/tensorflow:1.0-py3 -f Dockerfile-py3 .`
* Python 3 GPU: `docker build -t floydhub/tensorflow:1.0-gpu-py3 -f Dockerfile-py3.gpu .`

To push images to Docker registry:
* Python 2: `docker push floydhub/tensorflow:latest-py2`
* Python 2 GPU: `docker push floydhub/tensorflow:latest-gpu-py2`
* Python 3: `docker push floydhub/tensorflow:latest-py3`
* Python 3 GPU: `docker push floydhub/tensorflow:latest-gpu-py3`