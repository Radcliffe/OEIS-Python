# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A175972

from somewhere import primegen
for p in primegen():
    if all(str(p**k).count('1') == 2 for k in range(1, 7)):
        print(p) # _Lucas A. Brown_, Mar 23 2024

