# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A060957

from functools import cache
@cache
def s(n): return {1} if n == 0 else s(n-1) | set(x*n for x in s(n-1))
def a(n): return len(s(n))
print([a(n) for n in range(30)]) # _Michael S. Branicky_, Jul 31 2022 after _Alois P. Heinz_

