# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A383976

a = lambda n: int(bin(n)[2:].replace('1','3').replace('0','2'),4)
print([a(n) for n in range(0,51)])

