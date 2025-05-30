# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A361312

from sympy import isprime, nextprime
p = 1; mx = 5; I = [*range(mx)]; R = [*range(mx)]
while I:
    p = nextprime(p); ct = 0; q = p
    while isprime(int(bin(q)[2:])): ct += 1; q = int(bin(q)[2:])
    if ct in I: R[ct] = p; I.remove(ct)
print(*R, sep = ", ")

