# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A345018

from sympy import integer_nthroot
def A345018(n): return n-1+(k:=(m:=integer_nthroot(3*n,3)[0])+(6*n>m*(m+1)*((m<<1)+1)))*(k*(3-(k<<1))+5)//6 # _Chai Wah Wu_, Nov 05 2024

