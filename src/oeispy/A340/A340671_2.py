# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A340671

# see link for faster version
from bisect import insort
from num2words import num2words
from itertools import count, islice
def n2w(n): # remove " and" and commas
    return num2words(n).replace(" and", "").replace(", ", " ")
def agen(): # generator of terms
    names = [] # a sorted list
    for n in count(1):
        insort(names, (n2w(n), n-1))
        fixed = [j+1 for j in range(n) if names[j][1] == j]
        yield len(fixed) # use "yield fixed" for list of fixed points
print(list(islice(agen(), 87))) # Michael S. Branicky, Jul 05 2024

