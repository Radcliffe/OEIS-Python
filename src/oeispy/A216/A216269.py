# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A216269

import math
for i in range(1<<30):
    t = i*(i+1)*(i+2)//6 + 1
    sr = int(math.sqrt(t))
    if sr*sr == t:
        print(sr)

