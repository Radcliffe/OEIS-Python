# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A372394

from sympy import Matrix, jacobi_symbol
def A372394(n): return Matrix(n-1<<1,n-1<<1,[jacobi_symbol(i*(i+5*j+14)+j*(5*j+30)+44,(n<<1)|1) for i in range(n-1<<1) for j in range(n-1<<1)]).det() # _Chai Wah Wu_, Apr 30 2024

