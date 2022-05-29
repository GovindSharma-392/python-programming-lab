#Find the total occurrences of a specific word from a text file:
def program():
    cnt = 0
    word_search = input("Enter the words to search:")
    with open(r"C:\Users\HP\Desktop\python\basic\last\you.txtt","r") as f1:
        for data in f1:
            words = data.split()
            for word in words:
                if (word == word_search):
                    cnt+=1
    print(word_search, "found ", cnt, " times from the file")
program()