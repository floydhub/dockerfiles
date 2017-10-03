#!/bin/bash
set -euo pipefail

echo "Running tests..."
echo "OpenCV"
python -c "import cv2"
echo "gym"
python -c "import gym"
echo "nltk"
python -c "import nltk"
echo "pattern"
TEST_PATTERN="
import sys
if sys.version_info[0] < 3:
    import pattern
"
python -c "${TEST_PATTERN}"
echo "scikit-image"
python -c "import skimage"
echo "spacy"
python -c "import spacy"
echo "universe"
python -c "import universe"
echo "xgboost"
python -c "import xgboost"
echo "test kaggle-cli"
kg config
