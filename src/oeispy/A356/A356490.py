# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356490

from sympy import Matrix, prime
def A356490(n): return Matrix(n,n,[prime(abs(i-j)+1) for i in range(n) for j in range(n)]).det() # _Chai Wah Wu_, Aug 12 2022

