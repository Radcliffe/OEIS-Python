# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A179622

from functools import cache
@cache
def a(n): return 1 if n<10 else sum(a(n-int(i)) for i in str(n) if i!='0')
print([a(n) for n in range(1, 81)]) # _Michael S. Branicky_, Nov 12 2022

