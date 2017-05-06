from __future__ import print_function


import hashlib
import sys
import requests
import os
from shell import ex

JOB_LIST_DIR = 'ci/jobs'


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
            # TODO: support base image
            if 'dl/dl-base' in l:
                print('FIXME: Skipping base image: %s' % l)
                continue
            changed_dockerfiles.append(l)

    changed_dockerfiles.sort()
    return changed_dockerfiles


if not os.path.isdir(JOB_LIST_DIR):
    os.mkdir(JOB_LIST_DIR)

for dockerfile_path in find_changed_dockerfiles():
    job_id = hashlib.sha224(dockerfile_path).hexdigest()
    print('Creating jobs file %s for %s...' % (job_id, dockerfile_path))
    with open(os.path.join(JOB_LIST_DIR, job_id + '.job'), 'w') as f:
        f.write(dockerfile_path)
