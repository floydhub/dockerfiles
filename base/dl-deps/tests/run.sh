#!/bin/bash
set -euo pipefail

echo "Running tests..."
echo "bazel"
bazel version
echo "cmake"
cmake --version
echo "gfortran"
gfortran --version
