# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342349

from multiset import Multiset
from sympy import prime
A342349_list = []
for i in range(1,10**6):
    p = prime(i)
    q = p**3
    if Multiset(str(p)) <= Multiset(str(q)):
        A342349_list.append(q)

