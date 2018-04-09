#!/bin/bash
set -euo pipefail

echo "Running tests..."
echo "Testing OpenCV..."
python -c "import cv2"

echo "Testing gym..."
python -c "import gym"

echo "Testing nltk..."
python -c "import nltk"

echo "Testing pattern..."
TEST_PATTERN="
import sys
if sys.version_info[0] < 3:
    import pattern
"
python -c "${TEST_PATTERN}"

echo "Testing scikit-image..."
python -c "import skimage"

echo "Testing spacy..."
python -c "import spacy"

echo "Testing xgboost..."
python -c "import xgboost"

echo "Testing kaggle-cli..."
kg config
