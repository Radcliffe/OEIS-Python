# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A179993

from itertools import islice, takewhile, count
from sympy import isprime, divisors
def A179993(): # generator of terms
    for m in count(1):
        if all(isprime(m//a-a) for a in takewhile(lambda x: x*x <= m, divisors(m))):
            yield m
A179993_list = list(islice(A179993(),20)) # _Chai Wah Wu_, Nov 15 2021

