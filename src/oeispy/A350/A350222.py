# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350222

def A350222(n): return (m:=n**3)+sum(m//k**3 if k&1 else -(m//k**3) for k in range(2,n+1)) # _Chai Wah Wu_, Oct 27 2023

