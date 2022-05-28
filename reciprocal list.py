#WAP to find reciprocal of all elements of list.
ls = list(map(int,input().split()))
out = []
for i in ls:
    r = 1/int(i)
    out.append(r)
print(out)