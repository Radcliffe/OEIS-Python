# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A059953

def out_shuffle(deck):
  shuffle = [i for i in range(len(deck))]
  shuffle[0::2] = deck[:(len(deck)+1)//2]
  shuffle[1::2] = deck[(len(deck)+1)//2:]
  return shuffle
print(out_shuffle(range(1, 53))) # _Michael S. Branicky_, Jan 27 2021

