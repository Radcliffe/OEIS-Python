# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350201

from sympy import prime,nextprime,Matrix
def A350201(n):
    p = [prime(j) for j in range(1,2*n)]
    while Matrix(n,n,lambda i,j:p[i+j]).det():
        del p[0]
        p.append(nextprime(p[-1]))
    return p[0]

