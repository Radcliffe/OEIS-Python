# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A203601

a=1
for n in range(55):
    print(a, end=',')
    a ^= a*7

