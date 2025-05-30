# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A052035

# second version for going to large terms
from sympy import isprime
from itertools import product
def ok(pal):
    return isprime(pal) and isprime(sum(int(d)**2 for d in str(pal)))
def agentod(maxdigs):
    yield 11
    for d in range(3, maxdigs+1, 2):
        pal = 10**(d-1) + 1
        if ok(pal): yield pal
        for first in "1379":
            for left in product("0123456789", repeat=(d-3)//2):
                left = "".join(left)
                for mid in "13579":
                    pal = int(first + left + mid + left[::-1] + first)
                    if ok(pal): yield pal
print([an for an in agentod(5)]) # _Michael S. Branicky_, Nov 23 2021

