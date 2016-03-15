#!/usr/bin/env bash

EXPECTED='cat > caw > cay > coy > cry > dry > fry'
OUTPUT=$(python wordpaths.py cat fry)

if [ "$EXPECTED" == "$OUTPUT" ]; then
    echo "Output test OK"
else
    echo "Output test FAIL" "('$EXPECTED' != '$OUTPUT')"
fi
