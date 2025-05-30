# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A116381

from sympy import isprime
from sympy.utilities.iterables import partitions, multiset_permutations
def a(n):
    c = 0
    for p in partitions(n):
        plst = [k for k in p for _ in range(p[k])]
        s = sum(sum(map(int, str(pi))) for pi in plst)
        if s != 3 and s%3 == 0: continue
        for m in multiset_permutations(plst):
            if isprime(int("".join(map(str, m)))):
                c += 1
    return c
print([a(n) for n in range(1, 22)]) # _Michael S. Branicky_, Nov 19 2022

