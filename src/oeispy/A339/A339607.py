# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A339607

def aupto(n):
  alst, used = [1], {1}
  for i in range(2, n+1):
    binprev = bin(alst[-1])[2:]
    binwt = binprev.count("1")
    targetstr = bin(binwt)[2:]
    morebits, extra, ai = 0, 0, binwt
    while ai in used:
      morebits += 1
      found = False
      for k in range(2**morebits):
        binstrk = bin(k)[2:]
        binstrk = "0"*(morebits-len(binstrk)) + binstrk # pad to length
        for msbs in range(morebits+1):
          trystr = binstrk[:msbs] + targetstr + binstrk[msbs:]
          if trystr[0] == "0": continue
          trynum = int(trystr, 2)
          if trynum not in used:
            if not found: ai = trynum; found = True
            else: ai = min(ai, trynum)
      if found: break
    alst.append(ai); used.add(ai)
  return alst    # use alst[n-1] for a(n)
print(aupto(68)) # _Michael S. Branicky_, Dec 16 2020

