# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A097805

from math import comb
def T(n, k): return comb(n-1, k-1) if k != 0 else k**n  # _Peter Luschny_, May 06 2022

