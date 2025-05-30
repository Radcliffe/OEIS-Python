# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A380119

from dataclasses import dataclass
@dataclass
class Walk: s: str = ""; x: int = 0; y: int = 0
def Trow(n: int) -> list[int]:
    W = [Walk()]
    row = [0] * (n + 1)
    for w in W:
        if len(w.s) == 2*n:
            if w.x == w.y: row[w.y] += 1
        else:
            for s in "NSWE":
                x = y = 0
                match s:
                    case "W": x =  1
                    case "E": x = -1
                    case "N": y =  1
                    case "S": y = -1
                    case _  : pass
                if (w.y + y >= 0) and (w.x + x >= 0):
                    W.append(Walk(w.s + s, w.x + x, w.y + y))
    return row
for n in range(6): print(Trow(n))

