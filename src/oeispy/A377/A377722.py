# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A377722

from sympy import integer_nthroot
def A377722(n): return (m:=integer_nthroot(5*n,5)[0])+(30*n>m*(m+1)*((m<<1)+1)*(3*m*(m+1)-1))

