# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A063850

from collections import Counter; s = '1'
for _ in range(25):
    print(s, end = ', '); d = Counter(s); s = ''
    for k, v in d.items(): s += str(v) + k  # _Ya-Ping Lu_, Jun 06 2025

