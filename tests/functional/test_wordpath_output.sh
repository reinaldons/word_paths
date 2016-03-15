#!/usr/bin/env bash

# Valid word path
EXPECTED='cat > caw > cay > coy > cry > dry > fry'
OUTPUT=$(python wordpaths.py cat fry)

if [ "$EXPECTED" == "$OUTPUT" ]; then
    echo "Valid word path test OK"
else
    echo "Valid word path test FAIL" "('$EXPECTED' != '$OUTPUT')"
fi

# Valid path with one letter
EXPECTED='a > b > c > d > e > f > g > h > i > j > k > l > m > n > o > p > q > r > s > t > u > v > w > x > y > z'
OUTPUT=$(python wordpaths.py a z)

if [ "$EXPECTED" == "$OUTPUT" ]; then
    echo "Valid path with one letter test OK"
else
    echo "FAIL! Where is the Alphabet?"
fi

# Invalid word path
EXPECTED='four and nine have no viable path between them.'
OUTPUT=$(python wordpaths.py four nine)

if [ "$EXPECTED" == "$OUTPUT" ]; then
    echo "Invalid word path test OK"
else
    echo "Invalid word path test FAIL" "('$EXPECTED' != '$OUTPUT')"
fi
