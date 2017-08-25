#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function

import sys
import os
import logging
import click
import click_log
from .utils import (
    gen_tag_from_filepath, find_dockerfiles_in_project_dir, find_project_dirs
)

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


@click.command()
@click.argument('search_root')
@click.option('--tag-only/--no-tag-only',
              help='only display image tags',
              default=False)
@click_log.simple_verbosity_option(logger)
def tag(search_root, tag_only):
    """
    When --tag-only is not set, list all tags indented under project.

    For example:

    ./dl/tensorflow:
            floydhub/tensorflow:1.1.0-py2_aws
            floydhub/tensorflow:1.1.0-gpu-py2_aws
            floydhub/tensorflow:1.1.0-py2
            floydhub/tensorflow:1.1.0-py3_aws
            floydhub/tensorflow:1.1.0-py3
            floydhub/tensorflow:1.1.0-gpu-py3_aws
    ./dl/caffe:
            floydhub/caffe:1.0-gpu-py2
            floydhub/caffe:1.0-py2
            floydhub/caffe:1.0-py3
            floydhub/caffe:1.0-gpu-py3
    """
    for directory in find_project_dirs(search_root):
        if not tag_only:
            print(directory + ':')
        for dockerfile in find_dockerfiles_in_project_dir(directory):
            dockerfile_path = os.path.join(directory, dockerfile)
            if not tag_only:
                sys.stdout.write('\t')
            print(gen_tag_from_filepath(dockerfile_path))


@click.command()
@click.argument('search_root')
@click.option('--file-only/--no-file-only',
              help='only display dockerfile names',
              default=False)
@click_log.simple_verbosity_option(logger)
def dockerfile(search_root, file_only):
    """
    When --file-only is not set, list all dockerfiles indented under project.

    For example:

    ./dl/tensorflow:
            ./dl/tensorflow/1.1.0/Dockerfile-py2_aws
            ./dl/tensorflow/1.1.0/Dockerfile-py2.gpu
            ./dl/tensorflow/1.1.0/Dockerfile-py2
            ./dl/tensorflow/1.1.0/Dockerfile-py3_aws
            ./dl/tensorflow/1.1.0/Dockerfile-py3
            ./dl/tensorflow/1.1.0/Dockerfile-py3.gpu
    ./dl/caffe:
            ./dl/caffe/1.0/Dockerfile-py2.gpu
            ./dl/caffe/1.0/Dockerfile-py2
            ./dl/caffe/1.0/Dockerfile-py3
            ./dl/caffe/1.0/Dockerfile-py3.gpu
    """
    for directory in find_project_dirs(search_root):
        if not file_only:
            print(directory + ':')
        for dockerfile in find_dockerfiles_in_project_dir(directory):
            if not file_only:
                sys.stdout.write('\t')
            print(dockerfile)


@click.group('list')
def list_cmd():
    pass

list_cmd.add_command(tag)
list_cmd.add_command(dockerfile)
