# Write a program to display the largest word from the string.
a=input("Enter any String :")
L = a.split()
max=0
b=""
for i in L:
     if len(i) > max:
           b=i
           max=len(i)
print("Longest word is ",b)