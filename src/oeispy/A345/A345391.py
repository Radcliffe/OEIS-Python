# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A345391

def a(n):
    kn, ss = 2*n, set(str(n))
    while set(str(kn)) != ss: kn += n
    return kn
print([a(n) for n in range(1, 49)]) # _Michael S. Branicky_, Jun 17 2021

