# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A368744

def A368744(n): return ((n<<1)>>(~n & n-1).bit_length())-n # _Chai Wah Wu_, Jan 30 2024

