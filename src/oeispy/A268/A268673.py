# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A268673

def A268673(n): return (((m:=n-2)<<4)+(13 if m.bit_count()&1 else 5)) if n>1 else n # _Chai Wah Wu_, Mar 03 2023

