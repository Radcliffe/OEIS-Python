# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A187274

def A187274(n): return n<<n+1 if n&1 else 5*(n>>1)<<n # _Chai Wah Wu_, Feb 18 2024

