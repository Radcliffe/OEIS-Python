# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A226452

# see link for faster, bit-based version
from itertools import product
def closed(w): # w is a closed word
    if len(set(w)) <= 1: return True
    for l in range(1, len(w)):
        if w[:l] == w[-l:] and w[:l] not in w[1:-1]:
            return True
    return False
def a(n):
    if n == 0: return 1
    return 2*sum(closed("0"+"".join(b)) for b in product("01", repeat=n-1))
print([a(n) for n in range(22)]) # _Michael S. Branicky_, Jul 09 2022

