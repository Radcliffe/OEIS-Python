# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A117431

from sympy import S
def aupto(nn):
  phistr = str(S.GoldenRatio.n(nn+len(str(nn))+1)).replace(".", "")[:-1]
  for n in range(1, nn+1):
    nstr = str(n)
    if phistr[n-1:n-1+len(nstr)] == nstr: print(n, end=", ")
aupto(10**5) # _Michael S. Branicky_, Jan 20 2021

