# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A381522

from itertools import islice
def zeta_distribution_generator():
    num_ones, num_reached = 0, 1
    while num_ones := num_ones+1:
        yield 1
        for num in range(2, num_reached+2):
            if num_ones % (num*num) == 0:
                yield num
                num_reached += num == num_reached+1
A381522 = list(islice(zeta_distribution_generator(), 120))

