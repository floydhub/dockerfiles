#!/bin/bash
set -euo pipefail

echo "Testing nvcc..."
nvcc --version

echo "Testing libcudart.so..."
ls -lh /usr/local/cuda/lib64/libcudart.so

echo "Testing libcudnn.so..."
ls -lh /usr/lib/x86_64-linux-gnu/libcudnn.so
