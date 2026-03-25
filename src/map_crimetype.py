#!/usr/bin/env python3
import sys

for row in sys.stdin:
    row = row.strip()
    if not row:
        continue
    cols = row.split(',')
    if cols[0] == 'ID':
        continue
    if len(cols) > 5:
        ctype = cols[5].strip()
        if ctype:
            print(f"{ctype}\t1")
