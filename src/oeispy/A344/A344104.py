# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A344104

A344104_list, c = [10], 1
for _ in range(20):
    A344104_list.append(A344104_list[-1]*c)
    c += str(A344104_list[-1]).count('0') # _Chai Wah Wu_, Jun 06 2021

