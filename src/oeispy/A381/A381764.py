# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A381764

def A381764(n): return n^((a:=-n&n+1)|(a>>1))

