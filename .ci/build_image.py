#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function


import sys
from shell import ex
from subprocess import check_call


if len(sys.argv) <= 1:
    sys.exit('Missing argument! USAGE: %s JOB_FILE' % sys.argv[0])

job_file = sys.argv[1]
with open(job_file) as f:
    dockerfile_path, docker_tag = f.read().split()

print('--------------------------------------------')
print('[*] Building %s with tag %s...' % (dockerfile_path, docker_tag))
print('--------------------------------------------')
check_call('docker build -t %s -f %s .' % (docker_tag, dockerfile_path),
           shell=True)

print(ex('docker images').stdout())
