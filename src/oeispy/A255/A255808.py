# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A255808

def A255808(n):
    m = ((k:=7*n+1).bit_length()-1)//3
    return sum((1+((k-(1<<3*m))//(7<<3*j)&7))*9**j for j in range(m)) # _Chai Wah Wu_, Jun 28 2025

