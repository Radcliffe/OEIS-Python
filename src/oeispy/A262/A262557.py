# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A262557

from itertools import combinations
afull = list(map(int, sorted("".join(c) for i in range(1, 11) for c in combinations("9876543210", i)))) # _Michael S. Branicky_, Feb 13 2024

