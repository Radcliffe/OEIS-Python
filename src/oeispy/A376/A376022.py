# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376022

from itertools import count, islice
def a_gen():
    a = 1
    for n in count(2):
        yield a
        b = -1+(n*a)//(n+a)
        a = b
A376022_list = list(islice(a_gen(), 100)) # _John Tyler Rascoe_, Sep 17 2024

