#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import os

dockerfile_name_re = re.compile('Dockerfile-(?P<env>[^.]+)(?P<arch>(\.gpu)?)')


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
    if match.group('arch') == '.gpu':
        tag_components.append('gpu')
    tag_components.append(match.group('env'))

    return '-'.join(tag_components)


def find_matrix_from_dockerfile(dockerfile_path):
    abs_path = os.path.realpath(dockerfile_path)
    path_parts = abs_path.split(os.sep)
    return os.path.join(os.sep.join(path_parts[:-2]), 'matrix.yml')
