#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os


def test_gen_tag_from_filepath():
    from floydker.utils import gen_tag_from_filepath
    tag = gen_tag_from_filepath('dl/tensorflow/1.0.1/Dockerfile-py3.gpu')
    assert tag == 'floydhub/tensorflow:1.0.1-gpu-py3'

    tag = gen_tag_from_filepath('dl/../dl/tensorflow/1.0.1/Dockerfile-py3.gpu')
    assert tag == 'floydhub/tensorflow:1.0.1-gpu-py3'

    tag = gen_tag_from_filepath(
        'dl/../dl/tensorflow/1.0.1/Dockerfile-py3.gpu_aws')
    assert tag == 'floydhub/tensorflow:1.0.1-gpu-py3_aws'

    tag = gen_tag_from_filepath(
        'dl/../dl/tensorflow/1.0.1/Dockerfile-py2_aws')
    assert tag == 'floydhub/tensorflow:1.0.1-py2_aws'

    tag = gen_tag_from_filepath(
        'dl/tensorflow/1.4.0/Dockerfile-py3.gpu.cuda9cudnn7_aws')
    assert tag == 'floydhub/tensorflow:1.4.0-gpu.cuda9cudnn7-py3_aws'


def test_find_matrix_from_dockerfile():
    from floydker.utils import find_matrix_from_dockerfile
    matrix_path = find_matrix_from_dockerfile(
        'dl/tensorflow/1.0.1/Dockerfile-py3.gpu')

    assert os.sep.join(
        matrix_path.split(os.sep)[-3:]) == 'dl/tensorflow/matrix.yml'


def test_gen_target_env_from_tag():
    from floydker.utils import gen_target_env_from_tag
    target, env = gen_target_env_from_tag('tensorflow:1.0.1-gpu-py3')
    assert target == '1.0.1'
    assert env == 'py3.gpu'

    target, env = gen_target_env_from_tag('tensorflow:1.1.0-gpu-py3_aws')
    assert target == '1.1.0'
    assert env == 'py3.gpu_aws'

    target, env = gen_target_env_from_tag('floydhub/tensorflow:1.0.1-py2_aws')
    assert target == '1.0.1'
    assert env == 'py2_aws'

    target, env = gen_target_env_from_tag('floydhub/tensorflow:1.0.1-gpu.cuda11cudnn10-py2_aws')
    assert target == '1.0.1'
    assert env == 'py2.gpu.cuda11cudnn10_aws'
