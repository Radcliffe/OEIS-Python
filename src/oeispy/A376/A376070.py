# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376070

from sympy import  primefactors
def a(n, pn):
    if n == pn:
        return n
    else:
        return a(sum(primefactors(n)), n)
def A376070(n):
    k = 1
    result = n
    while result not in {4, 5, 7, 9}:
        result = 2 + a(result, None)
        k += 1
    if result in {5, 7, 9}:
        return k + 2
    else:
        return k
print([A376070(i) for i in range(1, 200)])

