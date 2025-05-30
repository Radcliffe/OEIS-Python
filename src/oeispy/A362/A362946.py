# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362946

from itertools import product
import math
max_term = 250
seq_set = set(range(1, max_term+1))
# Use the quadratic formula to calculate the maximum value for k,
# such that 1^1 + 2^1 + 3^1 + ... + k^1 is less than max_term.
max_k = int((-1 + math.sqrt(1 + 8 * max_term))/2.0) + 1
for k in range(1, max_k+1):
    list_of_exponent_ranges = [range(1,2)]
    for i in range(2, k+1):
        max_exponent = int(math.log(max_term, i))
        list_of_exponent_ranges.append(range(1, max_exponent+1))
    for exponents in product(*list_of_exponent_ranges):
        total = 0
        for i in range(1, k+1):
            total += int(i**exponents[i-1])
            if total > max_term:
                total = 0
                break
        if total in seq_set:
            seq_set.remove(total)
print(sorted(seq_set))

