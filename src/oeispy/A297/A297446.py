# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A297446

def A297446(n): return pow(3,n,(1<<n)-1)-1 if n>2 else n # _Chai Wah Wu_, Jun 25 2024

