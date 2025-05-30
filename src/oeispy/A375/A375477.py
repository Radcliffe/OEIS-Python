# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A375477

from itertools import count, islice
def bgen(ds): # generator of terms with digital sum ds
    def A051885(n): return ((n%9)+1)*10**(n//9)-1 # due to Chai Wah Wu
    def A228915(n): # due to M. F. Hasler
        p = r = 0
        while True:
            d = n % 10
            if d < 9 and r: return (n+1)*10**p + A051885(r-1)
            n //= 10; r += d; p += 1
    k = A051885(ds)
    while True: yield k; k = A228915(k)
def agen(): # generator of terms
    an, ds_block, seen, link_set, min2 = 0, 0, set(), "123456789", 11
    while True:
        yield an
        seen.add(an)
        if ds_block == 8:
            while min2 in seen: min2 = 10*min2 - 9
            an, ds_an, link_an = min2, 2, "1"
        else:
            cand_ds = list(range(1, 9-ds_block)) + [10-ds_block]
            dsg = [0] + [bgen(i) for i in range(1, 11-ds_block)]
            dsi = [0] + [(next(dsg[i]), i) for i in range(1, 11-ds_block)]
            while True:
                k, ds_k = min(dsi[j] for j in cand_ds)
                if k not in seen:
                    sk, dst = str(k), ds_k + ds_block
                    if sk[0] in link_set:
                        if dst < 9 or (dst == 10 and k%10 != 0):
                            an, ds_an, link_an = k, ds_k, sk[-1]
                            break
                dsi[ds_k] = (next(dsg[ds_k]), ds_k)
        ds_block = ds_block + ds_an
        if ds_block == 10: ds_block, link_set = 0, link_an
        else: link_set = "123456789"
print(list(islice(agen(), 60)))

