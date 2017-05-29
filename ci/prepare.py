from __future__ import print_function


import hashlib
import sys
import requests
import os
import glob
from shell import ex

JOB_LIST_DIR = 'ci/jobs'


def find_changed_dockerfiles():
    """
    This function returns a list of changed dockerfiles since the last
    push on the current branch. It uses circleci API to fetch the list
    of new commits (compare string) and uses git diff/show to figue out what
    files has been changed.
    """
    # STEP 1: find out the git compare string
    build_num = os.environ.get('CIRCLE_BUILD_NUM')
    info_api = 'https://circleci.com/api/v1.1/project/github/%s/%s/%s' % (
        os.environ.get('CIRCLE_PROJECT_USERNAME'),
        os.environ.get('CIRCLE_PROJECT_REPONAME'),
        build_num
    )

    print('[*] Fetching build info from %s...' % info_api)
    re = requests.get(info_api)
    if re.status_code != 200:
        sys.exit('Failed to fetch metadata for current build!')

    build_info = re.json()
    # value of 'compare' key is a github compare URL, we are only interested in
    # the last part, i.e. the actual compare string
    git_compare_url = build_info['compare']
    if not git_compare_url:
        return []
    git_compare = git_compare_url.split('/')[-1]

    # STEP 2: construct command to generate changed list
    changed_dockerfiles = []

    print('[*] List of changed files since last push (%s):' % git_compare)
    # multiple commits will be in the form of '2d12a44065cc^...aa673a945a6a'
    if '...' in git_compare:
        # use git diff for multiple commits
        cmd = 'git diff --name-only %s' % git_compare
    else:
        # use git show for single commit
        cmd = 'git show --name-only %s' % git_compare
    print('Running comand: %s' % cmd)

    # STEP 3: iterate through list of changed files and filter
    # based on filename
    for l in ex(cmd).stdout().split():
        print(l)
        # only record dockerfiles
        if 'Dockerfile' in l:
            # TODO: support base image
            if 'dl/dl-base' in l:
                print('FIXME: Skipping base image: %s' % l)
                continue
            if os.path.exists(l.strip()):
                changed_dockerfiles.append(l)

    return changed_dockerfiles


if not os.path.isdir(JOB_LIST_DIR):
    os.mkdir(JOB_LIST_DIR)

for dockerfile_path in find_changed_dockerfiles():
    # Using dockerfile_path for filename would be a pain in the ass to work
    # with because it contains os.sep. Here, we run it through a hash function
    # to simplify it while still maintain the uniqueness.
    job_id = hashlib.sha224(dockerfile_path).hexdigest()
    print('Creating jobs file %s for %s...' % (job_id, dockerfile_path))
    with open(os.path.join(JOB_LIST_DIR, job_id + '.job'), 'w') as f:
        f.write(dockerfile_path)

rebuild_glob_pattern = os.environ.get('FORCE_REBUILD_GLOB')
if rebuild_glob_pattern:
    print(('[*] Found $FORCE_REBUILD_GLOB ENV VAR: %r, '
           'search for list of files to rebuild...') % (rebuild_glob_pattern))
    for matched_file in glob.glob(rebuild_glob_pattern):
        if 'Dockerfile' in matched_file:
            job_id = hashlib.sha224(matched_file).hexdigest()
            print('Creating jobs file %s for %s...' % (job_id, matched_file))
            with open(os.path.join(JOB_LIST_DIR, job_id + '.job'), 'w') as f:
                f.write(matched_file)
