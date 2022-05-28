import numpy as np
ls = list(map(float,input().split()))
a = np.array(ls)
out = a[::-1]
print(out)