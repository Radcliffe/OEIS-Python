# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A114390

def A114390(n): return (m:=n**2)^ (m&~-m)<<1 # _Chai Wah Wu_, Jun 29 2022

