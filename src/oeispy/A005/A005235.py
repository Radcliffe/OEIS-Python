# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A005235

from sympy import nextprime, primorial
def a(n): psharp = primorial(n); return nextprime(psharp+1) - psharp
print([a(n) for n in range(1, 59)]) # _Michael S. Branicky_, Jan 15 2022

