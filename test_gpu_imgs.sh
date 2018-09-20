#!/bin/bash
set -e
for tag in `docker images | grep gpu | awk '{ print $1 ":" $2 }'`; do
    floydker test ${tag}
done
times
