# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A243766

from sympy import isprime, primerange
from itertools import count, islice, product
def agen(): yield from (a*10**(2*i) + b*10**i + c for i in count(1) for a, b, c in product(primerange(10**(i-1), 10**i), repeat=3) if isprime(a+b+c))
print(list(islice(agen(), 42))) # _Michael S. Branicky_, Dec 04 2022

