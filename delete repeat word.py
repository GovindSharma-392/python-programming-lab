from socket import if_indextoname


s = input('enter a string: ')
l = s.split()
a = []
for i in l:
    if (s.count(i)>=1 and (i not in a)):
        a.append(i)
print(' '.join(a))