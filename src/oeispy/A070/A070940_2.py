# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A070940

def A070940(n): return n.bit_length()-(~n&n-1).bit_length() # _Chai Wah Wu_, Jul 13 2022

