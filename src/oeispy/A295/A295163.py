# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A295163

# Print numbers with higher ratio of max Collatz descendant to self
# than that of any previous number.
# First column is OEIS sequence A025587 (the starting numbers).
# Second column is this sequence (their max odd descendants).
# Third column is OEIS sequence A061523 (before truncation).
i = 1
max_ratio = 1.0
while(True):
    n = i
    max_n = n
    while n >= i: # Done as soon as we dip below starting point
        n = 3*n + 1
        max_n = max(n, max_n)
        while (n&1) == 0:
            n = n >> 1
    ratio = float(max_n) / i
    if ratio > max_ratio:
        max_ratio = ratio
        print(i, (max_n - 1)/3, max_ratio)
    i += 2
# _Howard A. Landman_, Nov 15 2017

