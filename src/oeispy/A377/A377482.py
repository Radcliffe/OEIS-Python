# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A377482

from sympy import*
def a(n):
 t=0
 while n not in (1,4) and not isprime(n):
  n=sum(p*e for p,e in factorint(n).items());t+=n
 return t or n

