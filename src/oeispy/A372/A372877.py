# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A372877

# This Jacobi symbol is also defined for even k and n = 0.
def JacobiSymbol(n, k):
    if n == 0 and k == 1: return 1
    if n == 0 or k % 2 == 0: return 0
    n %= k
    res = 1
    while n != 0:
        while n % 2 == 0:
            n //= 2
            if k % 8 in (3, 5): res = -res
        if n % 4 == 3 == k % 4: res = -res
        n, k = k % n, n
    return res if k == 1 else 0
for n in range(10): print([JacobiSymbol(n, k) for k in range(n + 1)])

