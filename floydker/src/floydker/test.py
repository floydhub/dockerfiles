#!/usr/bin/env python
# -*- coding:utf-8 -*-

from subprocess import check_call
import sys
import os
import logging
import click
import click_log
from .utils import assert_image_tag_from_dockerfile

logger = logging.getLogger(__name__)


@click.command()
@click.argument('dockerfile')
@click_log.simple_verbosity_option()
@click_log.init(__name__)
def test(dockerfile):
    image_tag = assert_image_tag_from_dockerfile(logger, dockerfile)
    dockerfile_dir = os.path.dirname(dockerfile)
    os.chdir(dockerfile_dir)

    logger.info('--------------------------------------------')
    logger.info('[*] Testing image %s...', image_tag)
    logger.info('--------------------------------------------')

    test_script = 'test.sh'
    if not os.path.exists(test_script):
        logger.info('No test found for image %s, skipped.', dockerfile)
        sys.exit(0)

    cmds = ['docker', 'run',
            '-v', '%s:/build_test' % os.path.abspath(os.getcwd()),
            image_tag,
            'bash', '-c', 'cd /build_test && bash test.sh']
    logger.debug('running test docker command: %s', cmds)
    check_call(cmds)
