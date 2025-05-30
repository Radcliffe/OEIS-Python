# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A116436

from sympy import isprime
from itertools import count, islice
def agen(): # generator of terms
    yield 1
    for k in count(2):
        t = 10**(k+1) + 1
        yield from (t//i for i in range(100, 10, -1) if t%i == 0)
print(list(islice(agen(), 25))) # _Michael S. Branicky_, Mar 26 2023 following Franklin T. Adams-Watters but removing factorization

