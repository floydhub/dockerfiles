#!/usr/bin/env python
# -*- coding:utf-8 -*-

from subprocess import check_call
import sys
import os
import logging
import yaml
import click
import click_log
from .utils import (
    assert_image_tag_from_dockerfile,
    find_matrix_from_dockerfile,
    gen_version_target_from_tag
)

logger = logging.getLogger(__name__)


@click.command()
@click.argument('dockerfile')
@click_log.simple_verbosity_option()
@click_log.init(__name__)
def test(dockerfile):
    image_tag = assert_image_tag_from_dockerfile(logger, dockerfile)
    matrix_yml_path = find_matrix_from_dockerfile(dockerfile)
    project_dir = os.path.dirname(matrix_yml_path)

    if not os.path.exists(matrix_yml_path):
        logger.error('matrix.yml not found in project dir: %s', project_dir)
        sys.exit(1)

    # switch to project dir where matrix.yml is located, we assume test files
    # are located relative matrix.yml
    os.chdir(project_dir)

    with open(matrix_yml_path) as matrix_fobj:
        matrix = yaml.load(matrix_fobj)

    version, target = gen_version_target_from_tag(image_tag)
    if version not in matrix:
        logger.error('version %s not found in matrix.', version)
        sys.exit(1)

    version_cfg = matrix[version]
    if target not in version_cfg:
        logger.error('taget %s not found in version %s', target, version)
        sys.exit(1)

    target_cfg = version_cfg[target]
    test_script = target_cfg.get('_test')
    if not test_script:
        logger.info('No test found for image %s, skipped.', dockerfile)
        sys.exit(0)

    test_script = os.path.abspath(test_script)
    if not os.path.exists(test_script):
        logger.info('Defined test script (%s) not found for image %s.',
                    test_script, image_tag)
        sys.exit(1)

    logger.info('--------------------------------------------')
    logger.info('[*] Testing image %s with script %s...',
                image_tag, test_script)
    logger.info('--------------------------------------------')

    # Spin up a docker container to test the given image. Here, we mount the
    # directory where the test files live into /build_test path inside the
    # container (-v) so the container has access to all test files
    cmds = ['docker', 'run',
            '-v', '%s:/build_test' % os.path.dirname(test_script),
            image_tag,
            'bash', '-c',
            'cd /build_test && bash %s' % os.path.basename(test_script)]
    logger.debug('running test docker command: %s', cmds)
    check_call(cmds)
