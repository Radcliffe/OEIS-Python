# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A272022

from sympy import isprime
from itertools import count, islice, permutations
def agen(): yield from (k for k in count(1) if len(set(s:=str(k)))!=1 and all((t:=int("".join(m)))==k or isprime(t) for m in permutations(s)))
print(list(islice(agen(), 45))) # _Michael S. Branicky_, Dec 29 2023

