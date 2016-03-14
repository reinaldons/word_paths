#!/usr/bin/env bash

EXPECTED='cat > cag > cog > dog'
OUTPUT=$(python wordpaths.py cat dog)

if [ "$EXPECTED" == "$OUTPUT" ]; then
    echo "Output test OK"
else
    echo "Output test FAIL" "('$EXPECTED' != '$OUTPUT')"
fi
