#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os


def test_gen_tag_from_filepath():
    from floydker.utils import gen_tag_from_filepath
    tag = gen_tag_from_filepath('dl/tensorflow/1.0.1/Dockerfile-py3.gpu')
    assert tag == 'floydhub/tensorflow:1.0.1-gpu-py3'

    tag = gen_tag_from_filepath('dl/../dl/tensorflow/1.0.1/Dockerfile-py3.gpu')
    assert tag == 'floydhub/tensorflow:1.0.1-gpu-py3'


def test_find_matrix_from_dockerfile():
    from floydker.utils import find_matrix_from_dockerfile
    matrix_path = find_matrix_from_dockerfile(
        'dl/tensorflow/1.0.1/Dockerfile-py3.gpu')

    assert os.sep.join(
        matrix_path.split(os.sep)[-3:]) == 'dl/tensorflow/matrix.yml'
