# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355551

def a(n): return 3*((1<<n) - 1 - n*(n+1)//2)+(n**2+1)//2

