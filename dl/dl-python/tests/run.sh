#!/bin/bash

set -euo pipefail

echo "Running tests..."
jupyter --version
echo "matplotlib"
python -c "import matplotlib"
echo "h5py"
python -c "import h5py"
echo "numpy"
python -c "import numpy"
echo "pandas"
python -c "import pandas"
echo "scipy"
python -c "import scipy"
echo "sklearn"
python -c "import sklearn"
echo "cupy"
python -c "import cupy; print(cupy.array([1, 2, 3]))"
