# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A381868

import sympy
def a(n):
   p=sympy.prime(n); s=p; c=1
   p=sympy.nextprime(p); s+=p; c+=1
   while not(sympy.isprime(s-2) and sympy.isprime(s)):p=sympy.nextprime(p); s+=p; c+=1
   return c

