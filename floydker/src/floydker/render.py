#!/usr/bin/env python
# -*- coding:utf-8 -*-

import click
import yaml
import jinja2
import os
import click_log
import logging
import copy

logger = logging.getLogger(__name__)


class FilesLoader(jinja2.BaseLoader):
    """
    FilesLoader takes a list of template files instead of search path and
    expose template files by filename.

    Problem with the builtin loaders is there is no filtering support. For us,
    we don't put all template files within one directory tree. So we need do
    filter file types when traversing the filesystem. The caller of this class
    is responsible for the filtering.

    This class also enables us to lookup template file by filename instead of
    file path, which makes matrix.yml easier to write and read. The downside is
    we need to make sure all filenames are unique.
    """

    def __init__(self, files):
        self.files = files

    def get_source(self, environment, template):
        for template_file in self.files:
            if os.path.basename(template_file) == template:
                with open(template_file) as f:
                    contents = f.read().decode('utf-8')
                mtime = os.path.getmtime(template_file)
                return (contents,
                        template_file,
                        lambda: mtime == os.path.getmtime(template_file))
        else:
            raise jinja2.TemplateNotFound(template)

    def list_templates(self):
        found = [os.path.basename(f) for f in self.files]
        return sorted(found)


def populate_target_env_cfg(target_cfg, target_env):
    """
    Read out context from target config then merge it with global magic context

    All keys in target config that starts with `_` is considered magic context
    and will be merged into each target_env config.
    """
    # we need to do deepcopy here because yaml extend operation is not a
    # deepcopy and we will be injecting new keys in the following for loop
    target_env_cfg = copy.deepcopy(target_cfg[target_env])
    for dkey, dval in target_cfg.iteritems():
        if dkey.startswith('_') and dkey not in target_env_cfg:
            target_env_cfg[dkey] = dval
    return target_env_cfg


def render_matrix(jinja2_env, matrix_dir):
    """
    The "entry point" of matrix.yml is the `$render` key. It defines a list of
    targets to render.

    target maps to project version, each target will generate one directory.
    Each non-magic key in a target is considered a target_env.

    target_env maps to <env, arch(cpu/gpu)> pair, one Dockerfile will be
    generated for each defined target_env.

    Sample matrix.yml:

    target_1.1.1:
      _template: foo.jinja
      py2:
        key1: foo
        key2: bar

    In the above example, key1 and key2 will be passed in as context to render
    foo.jinja and generate a `Dockerfile-py2` file under `target_1.1.1`
    directory.
    """
    logger.debug('Entered directory: %s.', matrix_dir)
    with open(os.path.join(matrix_dir, 'matrix.yml')) as f:
        try:
            matrix = yaml.load(f)
        except:
            logger.exception('Failed to load matrix from %s', matrix_dir)
            return

    project_name = os.path.basename(matrix_dir)
    logger.debug('[%s] Loaded matrix: %s', project_name, matrix)

    for target in matrix.get('$render', []):
        if not isinstance(target, str):
            logger.error('target name needs to be a str, %s(%s) found.',
                         target, type(target))
            continue

        logger.info('[%s] Loading target <%s>...', project_name, target)
        # target_cfg here describes how to render multiple images for a given
        # version of a project
        target_cfg = matrix[target]
        template_name = target_cfg['_template']
        template = jinja2_env.get_template(template_name)

        # create target directory for Dockerfiles
        target_dir = os.path.join(matrix_dir, target)
        if not os.path.isdir(target_dir):
            os.mkdir(target_dir)

        for k in target_cfg:
            if k.startswith('_'):
                # skip reserved/magic keys
                continue
            target_env = k
            dockerfile_name = 'Dockerfile-' + target_env
            dockerfile_path = os.path.join(target_dir, dockerfile_name)
            logger.info('[%s] Rendering target env <%s-%s> to %s...',
                        project_name, target, target_env, dockerfile_path)
            target_env_cfg = populate_target_env_cfg(target_cfg, target_env)
            logger.debug('[%s] Rendering template with context %s',
                         project_name, target_env_cfg)
            with open(dockerfile_path, 'w') as f:
                f.write(template.render(**target_env_cfg))
            logger.debug('[%s] after wrote matrix: %s', project_name, matrix)


@click.command()
@click.argument('search_root')
@click.option('--project', help='only render project matches the given name')
@click_log.simple_verbosity_option()
@click_log.init(__name__)
def render(search_root, project):
    template_paths = []
    matrix_dirs = []

    # traverse filesystem once and find out all matrix.yml and templates
    for cur_dir, dirs, files in os.walk(search_root):
        # TODO: hornor .gitignore
        for f in files:
            if f == 'matrix.yml':
                logger.info('Found matrix in %s', cur_dir)
                matrix_dirs.append(cur_dir)
            elif f.endswith('.jinja'):
                template_paths.append(os.path.join(cur_dir, f))

    # register templates with jinja environment
    jinja2_env = jinja2.Environment(loader=FilesLoader(template_paths))

    for maxtrix_dir in matrix_dirs:
        if project and os.path.basename(maxtrix_dir) != project:
            continue
        render_matrix(jinja2_env, maxtrix_dir)
