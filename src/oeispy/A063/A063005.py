# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A063005

def a(n):
    m, p, target = 0, 1, 2**n
    while p <= target:  m += 1; p *= 3
    return target - 3**(m-1)
print([a(n) for n in range(36)]) # _Michael S. Branicky_, Nov 19 2021

