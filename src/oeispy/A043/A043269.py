# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A043269

def A043269(n):
    if n == 1: return 0
    y = 10*(x:=10**(len(str(n>>1))-1))
    return int((s:=str(n-x))[-1])+(sum(int(d) for d in s[:-1])<<1) if n<x+y else sum(map(int,str(n-y)))<<1 # _Chai Wah Wu_, Jun 13 2024

