# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A324678

#Sequences A324660-A324692 generated by manipulating this trip function
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
def minorzero(x):
    if x:
        return min(x)
    return 0
#Actual sequence
def a(n):
    d=trip(n)
    return minorzero([i for i in d['stuck'] if i<0])

