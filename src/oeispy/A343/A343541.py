# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A343541

import sympy
def a_n(N):
    a_n=[2]
    for i in sympy.primerange(5, N+1):
        a_n.append(A338295(i-1))
    print(a_n)
def A338295(n):
    checker=0
    for b in range(n//2, 1,-1):
        checker=main_base_check(n, b)
        if checker!=0:
            break
    return checker
def main_base_check(m, b):
    while m!=0:
        if m%b == b-1:
            return b
        m = m//b
    return 0
a_n(500)

