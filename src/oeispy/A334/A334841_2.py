# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A334841

def A334841(n):
    return 2*bin(n)[-1:1:-2].count('1')-(len(bin(n))-1)//2 if n > 0 else 0 # _Chai Wah Wu_, Sep 03 2020

