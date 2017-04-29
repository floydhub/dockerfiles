from __future__ import print_function


import hashlib
import sys
import requests
import os
import re
from shell import ex

JOB_LIST_DIR = '.ci/jobs'


dockerfile_name_re = re.compile('Dockerfile-(?P<env>[^.]+)(?P<arch>(\.gpu)?)')


def gen_tag_from_filepath(dockerfile_path):
    # sample input: dl/tensorflow/1.0.1/Dockerfile-py3.gpu
    # sample output: floydhub/tensorflow:1.0.1-gpu-py3
    path_parts = dockerfile_path.split('/')
    if len(path_parts) < 4:
        return None

    framework = path_parts[1]
    version = path_parts[2]
    tag_components = ['floydhub/%s:%s' % (framework, version)]

    dockerfile_name = path_parts[-1]
    match = dockerfile_name_re.match(dockerfile_name)
    if match.group('arch') == '.gpu':
        tag_components.append('gpu')
    tag_components.append(match.group('env'))

    return '-'.join(tag_components)


def find_changed_dockerfiles():
    build_num = os.environ.get('CIRCLE_BUILD_NUM')

    info_api = 'https://circleci.com/api/v1.1/project/github/%s/%s/%s' % (
        os.environ.get('CIRCLE_PROJECT_USERNAME'),
        os.environ.get('CIRCLE_PROJECT_REPONAME'),
        build_num
    )

    print('Fetching build info from %s...' % info_api)
    re = requests.get(info_api)
    if re.status_code != 200:
        sys.exit('Failed to fetch metadata for current build!')

    build_info = re.json()

    git_compare = build_info['compare'].split('/')[-1]

    changed_dockerfiles = []

    print('List of changed files since last push (%s):' % git_compare)
    if '...' in git_compare:
        cmd = 'git diff --name-only %s' % git_compare
    else:
        # use git show for single commit
        cmd = 'git show --name-only %s' % git_compare

    for l in ex(cmd).stdout().split():
        print(l)
        if 'Dockerfile' in l:
            changed_dockerfiles.append(l)

    changed_dockerfiles.sort()
    return changed_dockerfiles


if not os.path.isdir(JOB_LIST_DIR):
    os.mkdir(JOB_LIST_DIR)

for dockerfile_path in find_changed_dockerfiles():
    docker_tag = gen_tag_from_filepath(dockerfile_path)
    if not docker_tag:
        print(('Skipping %s due to inconsistent '
               'naming convention...') % dockerfile_path)
        continue

    job_id = hashlib.sha224(dockerfile_path).hexdigest()
    print('Creating jobs file %s for %s...' % (job_id, dockerfile_path))
    with open(os.path.join(JOB_LIST_DIR, job_id + '.job'), 'w') as f:
        f.write(dockerfile_path)
        f.write('\n')
        f.write(docker_tag)
