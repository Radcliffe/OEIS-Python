# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A023416

def A023416(n): return n.bit_length()-n.bit_count() if n else 1 # _Chai Wah Wu_, Mar 13 2023

