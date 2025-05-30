# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A005150

import re
def lookandsay(limit, sequence = 1):
    if limit > 1:
        return lookandsay(limit-1, "".join([str(len(match.group()))+match.group()[0] for matchNum, match in enumerate(re.finditer(r"(\w)\1*", str(sequence)))]))
    else:
        return sequence
# lookandsay(3) --> 21
# _Nicola Vanoni_, Nov 29 2016

