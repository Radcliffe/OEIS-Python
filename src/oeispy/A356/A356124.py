# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356124

from itertools import count, islice
from math import isqrt
from sympy import bernoulli
def A356124_T(n,k): return ((s:=isqrt(n))*(s+1)*(bernoulli(k+1)-bernoulli(k+1,s+1))+sum(w**k*(k+1)*((q:=n//w)*(q+1))+(w*(bernoulli(k+1,q+1)-bernoulli(k+1))<<1) for w in range(1,s+1)))//(k+1)>>1
def A356124_gen(): # generator of terms
     return (A356124_T(k+1,n-k-1) for n in count(1) for k in range(n))
A356124_list = list(islice(A356124_gen(),30)) # _Chai Wah Wu_, Oct 24 2023

