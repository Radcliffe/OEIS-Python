# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A346276

from sympy import isprime
def auptod(digs):
  return [t for t in (int('1'*(m-1-i) + '7' + '1'*i) for m in range(5, digs+1) if m%3 != 0 for i in range(m)) if t%7 == 0]
print(auptod(19)) # _Michael S. Branicky_, Jul 22 2021

