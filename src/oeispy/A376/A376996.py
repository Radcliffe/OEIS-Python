# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376996

def a(num:int) -> int:
    count = 0
    maxnum = num
    while num > 1:
        if num%2 == 1:
            num = num*3 + 1
        while num%2 == 0:
            num //= 2
        if num > maxnum:
            count += 1
            maxnum = num
    return count

