# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A011956

def A011956(n): return A371992(n) - (A011954(n//2) if n&1 else A011955(n//2)+A011955(n//2-1))
# _M. F. Hasler_, May 27 2025

