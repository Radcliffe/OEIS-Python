# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A358159

from sympy import Matrix
def A358159(n): return Matrix(n,n,[i*j-i*j//3 for i in range(1,n+1) for j in range(1,n+1)]).per() if n else 1 # _Chai Wah Wu_, Nov 02 2022

