# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A383540

import numpy as np, pandas as pd
x = np.arange(1, 1+10**8)
y = pd.Series(np.sin(x) ** x)
A383540 = sorted([1+int(np.where(y==m)[0][0]) for m in set(y.cummax())])

