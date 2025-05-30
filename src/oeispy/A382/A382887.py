# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A382887

from itertools import count, islice
from sympy import isprime, divisors
def A382887_gen(): # generator of terms
    yield from filter(lambda k:any(isprime((k<<d)+1) and isprime((d<<k)+1) for d in divisors(k,generator=True)),count(1))
A382887_list = list(islice(A382887_gen(),10)) # _Chai Wah Wu_, Apr 15 2025

