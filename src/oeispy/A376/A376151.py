# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376151

def ok(n):
    d = list(map(int, str(n)))
    return d[0] + d[-1] < sum(d[1:-1])
print([k for k in range(282) if ok(k)]) # _Michael S. Branicky_, Sep 12 2024

