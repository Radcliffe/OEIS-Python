# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A089309

def A089309(n): return (~((m:=n>>(~n&n-1).bit_length())+1)&m).bit_length() # _Chai Wah Wu_, Jul 13 2022

