# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A360860

from itertools import accumulate
def A360860Row(n: int) -> list[int]:
    return list(accumulate(A360603Row(n)))
for n in range(8): print(A360860Row(n))

