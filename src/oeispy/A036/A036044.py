# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A036044

def comp(s): z, o = ord('0'), ord('1'); return s.translate({z:o, o:z})
def BCR(n): return int(comp(bin(n)[2:])[::-1], 2)
print([BCR(n) for n in range(75)]) # _Michael S. Branicky_, Jun 14 2021

