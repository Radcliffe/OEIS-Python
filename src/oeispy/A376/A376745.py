# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376745

from sympy import integer_nthroot
def A376745(n): return n+(m:=integer_nthroot(k:=n<<1,3)[0])-(k<=m*(m-1)*(m+2))

