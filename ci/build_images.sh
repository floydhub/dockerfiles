#!/bin/bash

ANSI_RED="\033[31;1m"
# shellcheck disable=SC2034
ANSI_GREEN="\033[32;1m"
ANSI_RESET="\033[0m"
# shellcheck disable=SC2034
ANSI_CLEAR="\033[0K"

retry_cmd() {
    local result=0
    local count=1
    set +e

    retry_cnt=2
    shift 1

    while [ $count -le "${retry_cnt}" ]; do
        [ $result -ne 0 ] && {
            echo -e "\n${ANSI_RED}The command \"$*\" failed. Retrying, $count of ${retry_cnt}${ANSI_RESET}\n" >&2
        }
        "$@"
        result=$?
        [ $result -eq 0 ] && break
        count=$((count + 1))
        sleep 1
    done

    [ $count -gt "${retry_cnt}" ] && {
        echo -e "\n${ANSI_RED}The command \"$*\" failed ${retry_cnt} times.${ANSI_RESET}\n" >&2
    }

    set -e
    return $result
}

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
        retry_cmd floydker build "${dockerfile}" || {
            echo "Failed building ${dockerfile}."
            kill -9 "${ALIVEPID}"
            exit 1
        }
    done <<< "${jobfiles}"

    echo "Done, killing keepalive process: pid(${PID})."
    kill -9 "${ALIVEPID}"
fi
