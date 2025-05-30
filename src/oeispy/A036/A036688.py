# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A036688

from math import isqrt
def a(n):
    suffixes = set()
    for k in range(isqrt(10 ** (n - 1)) + 1, 10 ** n):
        kk = k * k
        s = str(kk)[-n:]
        if "0" not in s and len(s) >= n:
            suffixes.add(s)
    return len(suffixes)
print([a(n) for n in range(1, 8)])  # _Michael S. Branicky_, May 18 2021

