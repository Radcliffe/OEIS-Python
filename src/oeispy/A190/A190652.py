# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A190652

from datetime import date
def ok(n): return sum(date.isoweekday(date(n, m, 13)) == 5 for m in range(1, 13)) == 2
print(list(filter(ok, range(1901, 2000)))) # _Michael S. Branicky_, Sep 12 2021

