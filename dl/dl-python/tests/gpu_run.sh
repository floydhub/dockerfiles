#!/bin/bash

bash ./run.sh
echo "cupy"
python -c "import cupy; print(cupy.array([1, 2, 3]))"
