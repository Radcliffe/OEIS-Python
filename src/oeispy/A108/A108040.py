# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A108040

# Uses function seidel from A008281.
def A108040row(n): return seidel(n)[::-1] if n % 2 else seidel(n)
for n in range(8): print(A108040row(n)) # _Peter Luschny_, Jun 01 2022

