#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="floydker",
    version="0.1.1",
    author="Floyd",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "floydker = floydker:cli",
            "floydker-render = floydker.render:render",
        ]
    }
)
