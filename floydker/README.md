floydker
========

Automation for floydhub docker images


Installation
------------

```bash
python setup.py install
```


Usage
-----

### Templatize dockerfile

1. Create a directory for the project, e.g. `dl/tensorflow`
2. Create a matrix.yml file, e.g. `dl/tensorflow/matrix.yml`
3. Create a jinja2 template, e.g. `dl/tensorflow/tensorflow/tensorflow-1.x.x.jinja`


### Render dockerfiles with templates

Render all docker images:

```bash
floydker render ..
```

Render dockerfiles for a specific project:

```bash
floydker render --project tensorflow ..
```


### Define tests for images

Just add a `_test` key under your target configuration. For example:

```yaml
0.1.11:
  _template: pytorch-0.x.x.jinja
  py2:
    arch: cpu
    baseimg: floydhub/dl-base:latest-py2
    cpver: cp27-none
    _test: tests/py2_test.sh
```

If test script path is not absolute, it will be relative to matrix.yml. Test
script's parent directory will be mounted into a test container under path
`/build_test`, so it will only have access to files in its own directory.
