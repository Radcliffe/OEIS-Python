# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A035928

def comp(s): z, o = ord('0'), ord('1'); return s.translate({z:o, o:z})
def BCR(n): return int(comp(bin(n)[2:])[::-1], 2)
def aupto(limit): return [m for m in range(limit+1) if BCR(m) == m]
print(aupto(3244)) # _Michael S. Branicky_, Feb 10 2021

