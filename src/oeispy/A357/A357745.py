# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A357745

def A357745(n): return ((n+3)**2 >> 4) + 1 if n % 8 != 1 else (n+3)**2 >> 4

