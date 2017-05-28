#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import os
import sys
import copy

dockerfile_name_re = re.compile('Dockerfile-(?P<env>[^.]+)(?P<arch>(\.gpu)?)')


def gen_target_cfg_items(target_cfg):
    """
    Convert target_cfg to list of target configs
    """
    if isinstance(target_cfg, list):
        # list of templates defined for this target
        return target_cfg
    elif isinstance(target_cfg, dict):
        # only one template defined for this target
        return [target_cfg]
    else:
        return None


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


def gen_target_env_cfg(target_cfg_items):
    """
    Yield envs in given target_cfg list
    """
    for target_cfg_item in target_cfg_items:
        for k in target_cfg_item:
            if k.startswith('_'):
                # skip reserved/magic keys
                continue
            target_env = k
            target_env_cfg = populate_target_env_cfg(target_cfg_item,
                                                     target_env)
            yield target_env, target_env_cfg


def find_project_dirs(search_root):
    for cur_dir, dirs, files in os.walk(search_root):
        # TODO: hornor .gitignore
        for f in files:
            if f != 'matrix.yml':
                continue
            yield cur_dir


def gen_tag_from_filepath(dockerfile_path):
    # sample input: dl/tensorflow/1.0.1/Dockerfile-py3.gpu
    # sample output: floydhub/tensorflow:1.0.1-gpu-py3
    abs_path = os.path.realpath(dockerfile_path)

    path_parts = abs_path.split(os.sep)

    if len(path_parts) < 4:
        return None
    # we only care about the last 4 segments
    path_parts = path_parts[-4:]

    project = path_parts[1]
    version = path_parts[2]
    tag_components = ['floydhub/%s:%s' % (project, version)]

    dockerfile_name = path_parts[-1]
    match = dockerfile_name_re.match(dockerfile_name)
    if not match:
        return None

    if match.group('arch') == '.gpu':
        tag_components.append('gpu')
    tag_components.append(match.group('env'))

    return '-'.join(tag_components)


def find_dockerfiles_in_project_dir(project_dir):
    for cur_dir, dirs, files in os.walk(project_dir):
        for f in files:
            if f.startswith('Dockerfile'):
                yield os.path.join(cur_dir, f)


def find_matrix_from_dockerfile(dockerfile_path):
    abs_path = os.path.realpath(dockerfile_path)
    path_parts = abs_path.split(os.sep)
    return os.path.join(os.sep.join(path_parts[:-2]), 'matrix.yml')


def assert_image_tag_from_dockerfile(logger, dockerfile):
    if os.path.isdir(dockerfile):
        logger.error('%s is a directory.', dockerfile)
        sys.exit(1)

    image_tag = gen_tag_from_filepath(dockerfile)
    if not image_tag:
        logger.error('Failed to generate image tag from filename: %s',
                     dockerfile)
        sys.exit(1)

    return image_tag


def gen_target_env_from_tag(img_tag):
    """
    sample input: 'tensorflow:1.0.1-gpu-py3'
    sample output: ('1.0.1', 'py3.gpu')
    """
    img_commit = img_tag.split(':')[-1]
    version, target = img_commit.split('-', 1)
    target = '.'.join(reversed(target.split('-', 1)))
    return version, target
