#!/bin/bash

# set -o xtrace

keepalive() {
    # Sometimes, circleci got stuck and there will be no build output for 10min,
    # which causes the build to fail.
    # TODO: Remove this hack when this issue is resolved.
    while true; do
        echo "[$(date)] keepalive heartbeat..."
        sleep 60
    done
}

jobfiles=$(find ./ci/jobs -name "*.job" | sort | awk "NR % ${CIRCLE_NODE_TOTAL} == ${CIRCLE_NODE_INDEX}")

if [ -z "${jobfiles}" ]; then
    echo "[*] More parallelism than tests"
else
    keepalive &
    ALIVEPID=$!

    while read -r line; do
        echo "[*] Node ${CIRCLE_NODE_INDEX} running job ${line}..."
        dockerfile=$(cat "${line}")
        floydker build "${dockerfile}" || {
            echo "Failed building ${dockerfile}."
            kill -9 "${ALIVEPID}"
            exit 1
        }
    done <<< "${jobfiles}"

    echo "Done, killing keepalive process: pid(${PID})."
    kill -9 "${ALIVEPID}"
fi
