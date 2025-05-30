# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A263129

import itertools
decimal = []
huf = ['000','001','010','011','100','101','110','111']
  # This huf list has been processed by a Huffman coding function.
  # In order to find all the eight n different digits numbers, as I say
  # in Comments, this is the only Huffman encoding valid wordset, so this
  # is the simplest example routine.
ndec = list(map("".join, itertools.permutations('0123456789',len(huf))))
nbin = list(map("".join, itertools.permutations(huf)))
for item in nbin:
  decimal.append(str(int(item, 2)))
n = set(decimal).intersection(set(ndec))
print(sorted(n), len(n))
# _Francesco Di Matteo_, Oct 18 2015

