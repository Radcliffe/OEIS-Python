# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350330

from sympy import Matrix
from itertools import count
def A350330_list(nmax):
    a=[]
    for n in range(nmax):
        a.append(next(k for k in count(1) if all(Matrix((n-r)//2+1,(n-r)//2+1,lambda i,j:(a[r:]+[k])[i+j]).det()!=0 for r in range(n-2,-1,-2))))
    return a

