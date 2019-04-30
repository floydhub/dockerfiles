# Dockerfiles

Collection of Dockerfiles useful for NLP and Deep Learning. To download the docker images
visit: [floydhub's Docker Hub](https://hub.docker.com/r/floydhub/).


## How to update framework

1. Dockerfiles are generated using two inputs: `matrix.yml` and jinja template file inside `./dl/FRAMEWORK` directory. `matrix.yml` provides variable values for jinja template files.
  * The `$render` list in `matrix.yml` controls what version of the framework to render.
  * For each version config in `matrix.yml`, any key starts with `_` are global keys, which will get automatically injected into each variant config for that version.

2. Most of the cases, you only need to update `./dl/FRAMEWORK/matrix.yml` to generate a set of dockerfiles for a new version of a framework. If not, you will need to update the jinja file to account for build step changes.

3. Install floydker: `cd floydker && pipenv shell && pipenv install`.

4. Render dockerfiles: `cd .. && floydker render .`.

5. Commit new docker images to git and push: `git commit -a`.


## Naming conventions

Dockerfiles are organized into the following directory structure:

```
CATEGORY/PROJECT_NAME/VERSION/Dockerfile-ENV
CATEGORY/PROJECT_NAME/VERSION/Dockerfile-ENV.gpu
```

Automated build scripts will generate the following tags for images based on
the above dockerfile paths:

```
floydhub/PROJECT_NAME:VERSION-ENV
floydhub/PROJECT_NAME:VERSION-ENV-gpu
```

Contains docker images for popular deep learning frameworks including: Tensorflow, PyTorch and Torch.
