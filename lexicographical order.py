#sort elements in lexicograohical order
def sort(str):
    word = str.split()
    word.sort()
    for i in word:
        print(i)
str = 'this is India'
sort(str)