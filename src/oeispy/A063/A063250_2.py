# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A063250

def A063250(n): return 0 if (t:=bin(n)[2:].find('0'))==-1 else n.bit_length()-t # _Chai Wah Wu_, Mar 09 2025

