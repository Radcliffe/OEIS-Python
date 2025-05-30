# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A066736

import sympy
from sympy import factorint
def DigitProd(x):
  total = 1
  for i in str(x):
    total *= int(i)
  return total
def Prod(x):
  n = 2
  while n < 4*(10**8):
    if DigitProd(n**x) != 0 and DigitProd(n**x) != 1:
      count = 0
      for i in list(factorint(DigitProd(n**x)).values()):
        if (int(i)/x) % 1 == 0:
          count += 1
        else:
          break
      if count == len(list(factorint(DigitProd(n**x)).values())):
        return n
      else:
        n += 1
    else:
      n += 1
x = 1
while x < 100:
  print(Prod(x))
  x += 1 # _Derek Orr_, Feb 13 2014

