# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A116444

from sympy import isprime
from itertools import count, islice
def agen(): # generator of terms
    yield from [1, 3, 9]
    for k in count(2):
        t = 9*(10**(k+1) + 1)
        yield from (t//i for i in range(900, 90, -1) if t%i == 0)
print(list(islice(agen(), 38))) # _Michael S. Branicky_, Mar 26 2023

