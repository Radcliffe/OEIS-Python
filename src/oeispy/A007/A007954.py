# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A007954

from math import prod
def a(n): return prod(map(int, str(n)))
print([a(n) for n in range(108)]) # _Michael S. Branicky_, Jan 16 2022

