# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A352973

from sympy import isprime; R = []
for i in range(0, 1000):
    t = 2**i; L = []
    while t not in L: L.append(t); t = (t*t + 1) % 2**(i+1)
    {R.append(j) for j in {L[-1], L[-2]} if j not in R and isprime(j)}
R.sort(); print(*R, sep = ', ')

