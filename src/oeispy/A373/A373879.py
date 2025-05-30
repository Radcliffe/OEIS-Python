# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A373879

from sympy import gcd,isprime
def pollard_rho(n):
  x,y,d = 2,2,1
  f = lambda x: x*x-1
  while d==1:
    x = f(x) % n
    y = f(f(y)) % n
    d = gcd(abs(x-y),n)
  return d
isok = lambda n: not isprime(n) and pollard_rho(n) == n
print([n for n in range(4,3201) if isok(n)])

