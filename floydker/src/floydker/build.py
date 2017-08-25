#!/usr/bin/env python
# -*- coding:utf-8 -*-

from subprocess import check_call, check_output
import os
import logging
import click
import click_log
from .utils import assert_image_tag_from_dockerfile

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


@click.command()
@click.argument('dockerfile')
@click.option('--show-tag-only/--no-show-tag-only',
              help='skip build, only print out image tag name',
              default=False)
@click_log.simple_verbosity_option(logger)
def build(dockerfile, show_tag_only):
    image_tag = assert_image_tag_from_dockerfile(logger, dockerfile)
    if show_tag_only:
        print(image_tag)
        return

    dockerfile_dir = os.path.dirname(dockerfile)
    project_dir = os.path.dirname(dockerfile_dir)
    logger.info('--------------------------------------------')
    logger.info('[*] Building %s with tag %s...', dockerfile, image_tag)
    logger.info('--------------------------------------------')
    check_call('docker build --rm -t %s -f %s %s' % (image_tag,
                                                     dockerfile,
                                                     project_dir),
               shell=True)
    logger.info(check_output(['docker', 'images']))
