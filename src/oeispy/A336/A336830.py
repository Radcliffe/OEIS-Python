# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A336830

global arr
arr = []
def a(n):
    # Case 1
    if n == 0:
        return 0
    a_prev = arr[-1]
    cand = []
    # Case 2
    x = a_prev - n
    y = a_prev / n
    if x > 0 and not x in arr:
        cand.append(x)
    if y == int(y) and not y in arr:
        cand.append(y)
    if cand != []:
        return min(cand)
    # Case 3
    cand = []
    x = a_prev + n
    y = a_prev * n
    if not x in arr:
        cand.append(x)
    if not y in arr:
        cand.append(y)
    if cand != []:
        return min(cand)
    # Case 4
    return a_prev + n
def seq(n):
    for i in range(n):
        print("{}, ".format(a(i)), end="")
        arr.append(a(i))
seq(60)
# _Christoph B. Kassir_, Apr 08 2022

