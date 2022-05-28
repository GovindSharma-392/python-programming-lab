f = open(r'C:\Users\HP\Desktop\files\info.txt.txt','r')
data = f.readlines()
c = []
print(data)
print(len(data))
re = len(max(data,key = len))
for i in data:
    if len(i) == re:
        print(i)
f.close()