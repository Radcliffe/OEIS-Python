# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A352463

from math import prod
def ok(n): s = str(n); return s.startswith(str(prod(map(int, s))))
print([k for k in range(1, 12000) if ok(k)]) # _Michael S. Branicky_, Mar 17 2022

