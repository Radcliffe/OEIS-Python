# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A384538

def c(k, m): return (k > 0 and m%k == 0) or (m > 0 and k%m == 0)
def ok(n):
    s = str(n)
    return n > 9 and all(c(int(s[:i]), int(s[i:])) for i in range(1, len(s)))
print([k for k in range(150) if ok(k)]) # _Michael S. Branicky_, Jun 17 2025

