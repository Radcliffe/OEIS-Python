# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A116212

from sympy import divisors
def A116212_list(max_n):
    A116137,A116212,n = [1],[],0
    while len(A116212) < max_n:
        A116212.extend(divisors(A116137[-1]))
        A116137.append(A116137[-1]+A116212[n])
        n += 1
    return(A116212[:max_n]) # _John Tyler Rascoe_, Nov 18 2023

