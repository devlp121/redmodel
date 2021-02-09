

TESTDATA="$(pwd)/Dev/notebks/mh"


docker run -t --rm -p 8501:8501 \
    -v "$TESTDATA/savedmodel/redmodel:/models/redmodel" \
    -e MODEL_NAME=redmodel \
    tensorflow/serving &



