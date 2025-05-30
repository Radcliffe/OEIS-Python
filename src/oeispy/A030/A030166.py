# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A030166

from num2words import num2words
def A030166(n):
    kanji=['一','二','三','四','五','六','七','八','九','十','百','千','万','億','兆','京','垓','秭','穣','溝','澗','正','載','極','零']
    strokes=[1,2,3,5,4,4,2,2,2,2,6,3,3,15,6,8,9,10,18,13,15,5,13,12,13]
    return sum([strokes[kanji.index(i)] for i in num2words(n, lang='ja')]) # _Hunter N. Ratliff_, Feb 29 2020

