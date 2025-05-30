# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A084784

# after _Alois P. Heinz_
from functools import cache
from math import comb as binomial
@cache
def a(n: int) -> int:
    return 1 + sum((binomial(n, j) - a(n - j)) * a(j) for j in range(1, n))
print([a(n) for n in range(22)])  # _Peter Luschny_, Jun 09 2023

