# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A379938

import sympy
for (k, p) in enumerate(sympy.primerange(10**8)):
    rev = int(str(p)[::-1])
    # is rev a power of two (or zero)?
    if rev & (rev - 1) == 0:
        print(k + 1, end=",")
print()

