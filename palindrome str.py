#WAP to check given string is palindrome
def is_palindrome(s):
    return s==s[::-1]

s = input('enter string: ')
ans = is_palindrome(s)
if ans:
    print('palindrome')
else:
    print('not palindrome')