# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A285719

from sympy.ntheory.factor_ import core
def issquarefree(n): return core(n) == n
def a285718(n):
    if n==1: return 0
    x = 1
    while True:
        if issquarefree(x) and issquarefree(n - x):return x
        else: x+=1
def a285719(n): return n - a285718(n)
print([a285719(n) for n in range(1, 121)]) # _Indranil Ghosh_, May 02 2017

