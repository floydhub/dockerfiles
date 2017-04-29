#!/bin/bash

# set -o xtrace

jobfiles=$(find ./.ci/jobs -name "*.job" | sort | awk "NR % ${CIRCLE_NODE_TOTAL} == ${CIRCLE_NODE_INDEX}")

if [ -z "${jobfiles}" ]; then
    echo "[*] More parallelism than tests"
else
    while read -r line; do
        echo "[*] Node ${CIRCLE_NODE_INDEX} running job ${line}..."
        python .ci/build_image.py "${line}"
    done <<< "${jobfiles}"
fi
