# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A057889

def A057889(n): return int(bin(n>>(m:=(~n&n-1).bit_length()))[-1:1:-1],2)<<m # _Chai Wah Wu_, Dec 25 2024

