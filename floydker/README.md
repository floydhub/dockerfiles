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
