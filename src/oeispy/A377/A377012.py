# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A377012

import itertools
analys = range(1, 7) # increase this if you want
for limite in analys:
    numbers = range(pow(10,limite-1),pow(10,limite))
    r = range(1, limite+1)
    disp_temp = []
    for s in r:
        disp = list(itertools.product(r, repeat=s+1))
        disp_temp.extend(disp)
    disp_ok = [d for d in disp_temp if sum(d)==limite]
    for numero in numbers:
        str_numero = str(numero)
        for combo in disp_ok:
            k = limite
            totale = 0
            for c in range(len(combo), 0, -1):
                partenza = k-combo[c-1]
                porzione = str_numero[partenza:k]
                if c == 1:
                    totale = totale + int(porzione)
                else:
                    totale = totale + pow(int(porzione),c)
                k = k - combo[c-1]
            if totale == numero:
                print(numero)

