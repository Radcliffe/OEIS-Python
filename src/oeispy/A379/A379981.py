# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A379981

def ok(n):
    d = list(map(int, str(n)))
    return n and n%sum(d) and n%sum(di**2 for di in d)**2 == 0
print([k for k in range(10**6) if ok(k)]) # _Michael S. Branicky_, Jan 10 2025

