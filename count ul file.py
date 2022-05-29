#Count the total number of upper case, lower case, and digits used in the text file “merge.txt”.
def program():
    with open(r"C:\Users\HP\Desktop\python\basic\last\you.txt",'r') as f1:
       data=f1.read()
    cnt_ucase =0
    cnt_lcase=0
    cnt_digits=0
    for ch in data:
        if ch.islower():
            cnt_lcase+=1
        if ch.isupper():
            cnt_ucase+=1
        if ch.isdigit():
            cnt_digits+=1
    print(" Upper Case letters are:",cnt_ucase)
    print("Lower Case letters are:",cnt_lcase)
    print("digits are:",cnt_digits)
program()