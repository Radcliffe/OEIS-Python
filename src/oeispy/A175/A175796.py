# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A175796

def H(a, b, c):
    if c == 0: return b + 1
    if c == 1 and b == 0: return a
    if c == 2 and b == 0: return 0
    if c >= 3 and b == 0: return 1
    return H(a, H(a, b - 1, c), c - 1)
for n in range(5): print(H(n, 2, n))

