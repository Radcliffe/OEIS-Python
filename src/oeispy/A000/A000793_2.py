# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A000793

from sympy import primerange,sqrt,log,Rational
def f(N): # compute terms a(0)..a(N)
    V = [1 for j in range(N+1)]
    if N < 4:
        C = 2
    else:
        C = Rational(166,125)
    for i in primerange(C*sqrt(N*log(N))):
        for j in range(N, i-1, -1):
            hi = V[j]
            pp = i
            while pp <= j:
                hi = max(V[j-pp]*pp, hi)
                pp *= i
            V[j] = hi
    return V
# _Philip Turecek_, Mar 31 2023

