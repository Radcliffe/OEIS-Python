# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A331498

from num2words import num2words
import unidecode
def A331498(n):
    return ord(unidecode.unidecode(num2words(n, lang='fr')).lower()[0]) - 96 # _Chai Wah Wu_, Feb 27 2020

