# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A130232

A130232_list, c = [0], 1
for _ in range(100):
    A130232_list.append(A130232_list[-1]+c)
    c += str(A130232_list[-1]).count('0') # _Chai Wah Wu_, Jun 06 2021

