# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A269483

A269483_list, m = [], [479001600, -2674425600, 6386688000, -8501915520, 6889478400, -3482100720, 1080164160, -194177280, 17948256, -666714, 5418, 0, 1]
for _ in range(10**2):
    A269483_list.append(m[-1])
    for i in range(12):
        m[i+1] += m[i] # _Chai Wah Wu_, Feb 28 2016

