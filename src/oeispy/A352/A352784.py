# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A352784

def w(n): return bin(n).count("1")
def a(n): return w(n - w(n))
print([a(n) for n in range(108)]) # _Michael S. Branicky_, Apr 02 2022

