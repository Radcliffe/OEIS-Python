# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A385029

a = lambda n: ((n*n+n)*((n << 1)+1)**3)//3
print([a(n) for n in range(1, 11)])

