# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A228188

from sympy.ntheory.modular import crt
def A228188(n): return (k:=int(min(crt(m:=(1<<(n+1),5**n),(0,-1))[0], crt(m,(-1,0))[0])))*(k+1)>>1 # _Chai Wah Wu_, Jul 25 2022

