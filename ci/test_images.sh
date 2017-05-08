#!/bin/bash

echo "Testing..."

jobfiles=$(find ./ci/jobs -name "*.job" | sort | awk "NR % ${CIRCLE_NODE_TOTAL} == ${CIRCLE_NODE_INDEX}")

if [ -z "${jobfiles}" ]; then
    echo "[*] More parallelism than tests"
else
    while read -r line; do
        echo "[*] Node ${CIRCLE_NODE_INDEX} running test for job ${line}..."
        floydker test $(cat "${line}")
    done <<< "${jobfiles}"
fi
