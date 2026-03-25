#!/usr/bin/env python3
import sys

for row in sys.stdin:
    row = row.strip()
    if not row:
        continue
    cols = row.split(',')
    if cols[0] == 'ID':
        continue
    if len(cols) > 2:
        try:
            date_field = cols[2].strip()
            year = date_field.split(' ')[0].split('/')[2]
            print(f"{year}\t1")
        except (IndexError, ValueError):
            pass
