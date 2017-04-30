#!/usr/bin/env python
# -*- coding:utf-8 -*-

import yaml
import jinja2
import os
import sys

import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)-4s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


Env = None


class FilesLoader(jinja2.BaseLoader):
    """
    FilesLoader takes a list of template files instead of search path
    """

    def __init__(self, files):
        self.files = files

    def get_source(self, environment, template):
        for tpl_file in self.files:
            if os.path.basename(tpl_file) == template:
                with open(tpl_file) as f:
                    contents = f.read().decode('utf-8')
                mtime = os.path.getmtime(tpl_file)
                return (contents,
                        tpl_file,
                        lambda: mtime == os.path.getmtime(tpl_file))
        else:
            raise jinja2.TemplateNotFound(template)

    def list_templates(self):
        found = [os.path.basename(f) for f in self.files]
        return sorted(found)


def populate_target_cfg(build_cfg, build_target):
    """
    Read out context from target config then merge it with global magic context

    All keys in build config that starts with `_` is considered magic context
    and will be merged into build_target config.
    """
    build_target_cfg = build_cfg[build_target]
    for dkey, dval in build_cfg.iteritems():
        if dkey.startswith('_'):
            build_target_cfg[dkey] = dval
    return build_target_cfg


def build_matrix(matrix_dir):
    """
    The "entry point" of matrix.yml is the `build` key. It defines a list of
    builds to generate.

    build maps to image version, each build will generate one directory.
    Each non-magic key in build is considered a build_target.

    build_target maps to <env, arch(cpu/gpu)> pair, each build_target will
    generate one Dockerfile

    Sample matrix.yml:

    build:
      _tpl: foo.jinja
      build_target:
        key1: foo
        key2: bar

    In the above example, key1 and key2 will be passed in as context to render
    foo.jinja and generate `Dockerfile-build_target` file.
    """
    logger.info('Entered directory: %s.', matrix_dir)
    with open(os.path.join(matrix_dir, 'matrix.yml')) as f:
        try:
            matrix = yaml.load(f)
        except:
            logger.exception('Failed to load matrix from %s', matrix_dir)
            return

    image_name = os.path.basename(matrix_dir)
    logger.debug('[%s] Loaded matrix: %s', image_name, matrix)

    for build in matrix.get('build', []):
        if not isinstance(build, str):
            logger.error('Build name needs to be a str, %s(%s) found.',
                         build, type(build))
            continue

        logger.info('[%s] Loading build <%s>...', image_name, build)
        # build_cfg usually describes how to build multiple images for a given
        # version of framework
        build_cfg = matrix[build]
        tpl_name = build_cfg['_tpl']
        tpl = Env.get_template(tpl_name)

        # create build directory for Dockerfiles
        build_dir = os.path.join(matrix_dir, build)
        if not os.path.isdir(build_dir):
            os.mkdir(build_dir)

        for k in build_cfg:
            if k.startswith('_'):
                # skip reserved keys
                continue
            build_target = k
            logger.info('[%s] Building target <%s-%s>...',
                        image_name, build, build_target)
            build_target_cfg = populate_target_cfg(build_cfg, build_target)
            logger.debug('[%s] Rendering template with context %s',
                         image_name, build_target_cfg)
            dockerfile_path = os.path.join(build_dir,
                                           'Dockerfile-' + build_target)
            with open(dockerfile_path, 'w') as f:
                f.write(tpl.render(**build_target_cfg))


def main(project_root):
    global Env
    tpl_paths = []
    matrix_dirs = []

    for cur_dir, dirs, files in os.walk(project_root):
        # TODO: hornor .gitignore
        for f in files:
            if f == 'matrix.yml':
                logger.info('Found matrix in %s', cur_dir)
                matrix_dirs.append(cur_dir)
            elif f.endswith('.jinja'):
                tpl_paths.append(os.path.join(cur_dir, f))

    Env = jinja2.Environment(loader=FilesLoader(tpl_paths))

    for d in matrix_dirs:
        build_matrix(d)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = '.'
    main(project_root)
