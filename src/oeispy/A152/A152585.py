# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A152585

def A152585(n): return (1<<2*(m:=1<<n))*3**m+1 # _Chai Wah Wu_, Jul 19 2022

