# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A181134

A181134_list, m = [0], [6227020800, -37362124800, 97037740800, -142702560000, 130456085760, -76592355840, 28805736960, -6711344640, 901020120, -60780720, 1569750, -8190, 1, 0 , 0]
for _ in range(10**2):
    for i in range(14):
        m[i+1]+= m[i]
    A181134_list.append(m[-1]) # _Chai Wah Wu_, Nov 06 2014

