# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A136428

def A136428(n): return (f:=lambda m: int(''.join(map(lambda x:'0111222223'[int(x)], str(m)))))(n+1)-f(n) # _Chai Wah Wu_, Oct 19 2024

