# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349744

for n in range(1, 12):
    b = 10**n; M = set()
    for i in range(b):
        t = i; L = set()
        while t not in L: L.add(t); t = (t**3)%b
        d = len(L)
        if d not in M: M.add(d)
    print(len(M), end = ', ')

