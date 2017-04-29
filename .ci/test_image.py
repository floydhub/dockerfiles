#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function

import sys
import os

from subprocess import check_call


if len(sys.argv) <= 1:
    sys.exit('Missing argument! USAGE: %s JOB_FILE' % sys.argv[0])

job_file = sys.argv[1]
with open(job_file) as f:
    dockerfile_path, docker_tag = f.read().split()

dockerfile_dir = os.path.dirname(dockerfile_path)
test_script = os.path.join(dockerfile_dir, 'test.sh')

if not os.path.exists(test_script):
    print('No test found for image %s, skipped.' % dockerfile_path)
    sys.exit(0)

cmds = ['docker', 'run',
        '-v', '%s:/build_test' % os.path.abspath(dockerfile_dir),
        docker_tag,
        'bash', '-c', 'cd /build_test && bash test.sh']
print('running command: %s' % cmds)
check_call(cmds)
