# Python program to count vowels in a string
def countVowels(string):
    num_vowels=0
    for char in string:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels


string = input('Enter any string: ')
print('No of vowels =',countVowels(string))