# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A283845

from sympy import fibonacci
for n in range(1, 21):
    print([fibonacci(max(m, n - m + 1)) for m in range(1, n + 1)]) # _Indranil Ghosh_, Apr 01 2017

