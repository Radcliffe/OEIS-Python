# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A351565

def A351565(n): return (m:=1+(n>>(~n&n-1).bit_length()))>>(~m&m-1).bit_length()  # _Chai Wah Wu_, Jan 03 2024

