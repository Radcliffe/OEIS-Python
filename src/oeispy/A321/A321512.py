# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A321512

for n in range(1, 101):
   cards = [i for i in range(1, n + 1)]
   reverse = cards[::-1]
   shuffled = cards.copy()
   reversein = False
   for i in range(n):
      evens = shuffled[1::2]
      odds = shuffled[0::2]
      shuffled = evens + odds
      if shuffled == reverse:
         reversein = True
   print(n, int(reversein))

