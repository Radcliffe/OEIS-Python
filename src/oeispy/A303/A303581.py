# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A303581

def A303581(n): return (n.bit_count()&1)+n.bit_length() # _Chai Wah Wu_, Mar 02 2023

