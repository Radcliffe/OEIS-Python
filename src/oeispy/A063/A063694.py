# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A063694

def A063694(n): return n&((1<<(m:=n.bit_length())+(m&1))-1)//3 # _Chai Wah Wu_, Jan 30 2023

