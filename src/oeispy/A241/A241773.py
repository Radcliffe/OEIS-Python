# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A241773

from fractions import Fraction
def prob_count_diff(j, k, count):
    return  - ((1 - Fraction(1,(j+1)*(j+1)))**k) * (2**count)
def sample_pdf(n):
    coeffs, unreached_val, counts = [], 1, {}
    for k in range(1, n+1):
        prob_count_diffs = [prob_count_diff(i, k, counts.get(i, 0)) for i in range(1, unreached_val+1)]
        most_probable = prob_count_diffs.index(max(prob_count_diffs)) + 1
        unreached_val += most_probable == unreached_val
        coeffs.append(most_probable)
        counts[most_probable] = counts.get(most_probable, 0) + 1
    return coeffs
A241773 = sample_pdf(120)  # _Jwalin Bhatt_, Feb 09 2025

