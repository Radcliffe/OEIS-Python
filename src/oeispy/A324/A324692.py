# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A324692

import functools
#Sequences A324660-A324691 generated by manipulating this trip function
#spots - positions in order with possible repetition
#flee - positions from which we move away from zero with possible repetition
#stuck - positions from which we move to a spot already visited with possible repetition
def trip(n):
    stucklist = list()
    spotsvisited = [n]
    leavingspots = list()
    turn = 0
    forbidden = {n}
    while n != 0:
        turn += 1
        sign = n // abs(n)
        st = sign * turn
        if n - st not in forbidden:
            n = n - st
        else:
            leavingspots.append(n)
            if n + st in forbidden:
                stucklist.append(n)
            n = n + st
        spotsvisited.append(n)
        forbidden.add(n)
    return {'stuck':stucklist, 'spots':spotsvisited,
                'turns':turn, 'flee':leavingspots}
def sgn(x):
    if x:
        return x//abs(x)
    return 0
@functools.lru_cache(maxsize=None)
def A324672(n):
    d = trip(n)
    mx=max([i for i in d['spots']])
    mn=min([i for i in d['spots']])
    return sgn(mx+mn)
#Actual sequence
def a(n):
    return sum(A324672(i) for i in range(n))

