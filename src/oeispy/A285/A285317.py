# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A285317

from operator import mul
from functools import reduce
from sympy import prime
from sympy.ntheory.factor_ import core
def a019565(n): return reduce(mul, (prime(i+1) for i, v in enumerate(bin(n)[:1:-1]) if v == '1')) if n > 0 else 1
print([n for n in range(1, 5201) if core(n) == n and a019565(n) < n]) # _Indranil Ghosh_, Apr 18 2017, after _Chai Wah Wu_

