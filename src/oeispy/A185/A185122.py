# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A185122

from math import gcd
from itertools import count
from sympy import nextprime
from sympy.ntheory import digits
def A185122(n):
    m = n
    j = 0
    if n > 3:
        for j in range(1,n):
            if gcd((n*(n-1)>>1)+j,n-1) == 1:
                 break
    if j == 0:
        for i in range(2,n):
            m = n*m+i
    elif j == 1:
        for i in range(1,n):
            m = n*m+i
    else:
        for i in range(2,1+j):
            m = n*m+i
        for i in range(j,n):
            m = n*m+i
    m -= 1
    while True:
        if len(set(digits(m:=nextprime(m),n)[1:]))==n:
            return m # _Chai Wah Wu_, Mar 12 2024

