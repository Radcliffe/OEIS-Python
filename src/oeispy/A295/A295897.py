# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A295897

[x ^ (x>>1) for x in range(0,2048) if (x & (x<<1) == 0)]
# _Frédéric Nouvier_, Aug 14 2020

