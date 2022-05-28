import numpy as np
r,c = list(map(int,input().split()))
ls = list(map(int,input().split()))
arr = np.array(ls)
mt = arr.reshape(r,c)
tp = np.transpose(mt)
ft = mt.flatten()
print(tp)
print(ft)