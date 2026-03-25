#!/usr/bin/env python3
import sys

for row in sys.stdin:
    row = row.strip()
    if not row:
        continue
    cols = row.split(',')
    if cols[0] == 'ID':
        continue
    if len(cols) > 7:
        loc = cols[7].strip()
        if loc:
            print(f"{loc}\t1")
