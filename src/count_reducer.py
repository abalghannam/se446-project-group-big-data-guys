#!/usr/bin/env python3
import sys

prev = None
count = 0

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 2:
        continue
    word = parts[0]
    try:
        n = int(parts[1])
    except ValueError:
        continue

    if word == prev:
        count += n
    else:
        if prev is not None:
            print(f"{prev}\t{count}")
        prev = word
        count = n

if prev is not None:
    print(f"{prev}\t{count}")
