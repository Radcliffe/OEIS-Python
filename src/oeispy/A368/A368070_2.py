# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A368070

from fractions import Fraction as frac
inte=lambda p: [0]+[frac(c,i+1) for i,c in enumerate(p)]
from math import factorial as fact
def A368070(n):
  r=[1]
  for k in range(n.bit_length()):
    i=inte(r)
    r=i if n>>k&1 else [sum(i)]+[-c for c in i[1:]]
  return int(fact(n.bit_length()+1)*sum(inte(r)))
#without the multiplication, this is the probability that a sequence of real numbers in [0,1] satisfies the chain of inequalities. # _Natalia L. Skirrow_, Apr 20 2025

