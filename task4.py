import numpy as np
r,c = list(map(int,input().split()))
m1 = []
m2 = []
for i in range(r):
    ele = list(map(int,input().split()))
    m1.append(ele)
for i in range(r):
    ele = list(map(int,input().split()))
    m2.append(ele)
m1 = np.array(m1)
m2 = np.array(m2)
a = np.add(m1,m2)
s = np.subtract(m1,m2)
d = np.floor_divide(m1,m2)
p = np.power(m1,m2)
print(a)
print(s)
print(d)
print(p)
