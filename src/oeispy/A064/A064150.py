# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A064150

import numpy as np
def gen():
    for dec_num in range(1,153):
        tern_num = np.base_repr(dec_num, 3)
        sum_tern_digits = 0
        for i in tern_num:
            sum_tern_digits += int(i)
        if dec_num % sum_tern_digits == 0:
            yield dec_num
print(list((gen()))) # _Adrienne Leonardo_, Dec 28 2024

