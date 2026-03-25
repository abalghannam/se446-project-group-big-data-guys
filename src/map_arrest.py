#!/usr/bin/env python3
import sys

for row in sys.stdin:
    row = row.strip()
    if not row:
        continue
    cols = row.split(',')
    if cols[0] == 'ID':
        continue
    if len(cols) > 8:
        status = cols[8].strip().lower()
        if status in ('true', 'false'):
            print(f"{status}\t1")
