def anag(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print('anagram')
    else:
        print('not anagram')
s1 =input('enter str1: ')
s2 =input('enter str2: ')    
anag(s1,s2)