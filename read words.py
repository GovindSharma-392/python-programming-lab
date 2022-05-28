#write a python script to count no. of words in a given text file data.txt

f = open('C:\Users\HP\Desktop\hey.txt','r')
data = f.read()
words = data.split()
print(words)
print(len(words))
f.close()
