# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A070938

def ok(n):
    s = str(n)
    d = sum(map(int, s))
    return d and n%d == 0 and s.endswith(str(d))
print([k for k in range(10**4) if ok(k)]) # _Michael S. Branicky_, Jun 10 2024

