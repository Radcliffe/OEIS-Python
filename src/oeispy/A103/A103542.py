# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A103542

def a(n): return '0' if n<1 else bin(sum([(n + k)&(2**k) for k in range(len(bin(n)[2:]) + 1)]))[2:] # _Indranil Ghosh_, May 03 2017

