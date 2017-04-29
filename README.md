# Dockerfiles

Collection of Dockerfiles useful for NLP and Deep Learning. To download the docker images
visit: [Docker Hub][https://hub.docker.com/r/floydhub/]


## Usage

To generate all dockerfiles:

```bash
pip install -r requirements.txt
python floydker-build.py
```

## Naming conventions

All Dockerfiles should be organized in the following directory structure:

```
CATEGORY/IMAGE_NAME/VERSION/Dockerfile-ENV
CATEGORY/IMAGE_NAME/VERSION/Dockerfile-ENV.gpu
```

Automated build scripts will generate the following tags for images based on
the above dockerfile paths:

```
floydhub/IMAGE_NAME:VERSION-ENV
floydhub/IMAGE_NAME:VERSION-ENV-gpu
```
