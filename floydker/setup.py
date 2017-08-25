#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="floydker",
    version="0.1.0",
    author="Floyd",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        "click>=6.7",
        "click-log==0.2.0",
        "pyyaml",
        "jinja2",
    ],
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "floydker = floydker:cli",
            "floydker-render = floydker.render:render",
        ]
    }
)
