# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A351657

from math import lcm
from itertools import count
from sympy import factorint
def f(n,pe): # period of the Fibonacci n-step sequence mod pe
    a = b = (0,)*(n-1)+(1%pe,)
    s = 1 % pe
    for m in count(1):
        b, s = b[1:] + (s,), (s+s-b[0]) % pe
        if a == b:
            return m
def A351657(n): return 1 if n == 1 else lcm(*(f(n,p**e) for p, e in factorint(n).items())) # _Chai Wah Wu_, Feb 23-27 2022

