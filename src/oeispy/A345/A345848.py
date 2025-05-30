# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A345848

from itertools import combinations_with_replacement as cwr
from collections import defaultdict
keep = defaultdict(lambda: 0)
power_terms = [x**4 for x in range(1, 1000)]
for pos in cwr(power_terms, 9):
    tot = sum(pos)
    keep[tot] += 1
    rets = sorted([k for k, v in keep.items() if v == 6])
    for x in range(len(rets)):
        print(rets[x])

