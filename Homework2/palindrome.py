"""Determine if string is a palindrome."""
import re
string = input('Input string for palindrome check:')
regex = re.compile('\w|\d')
treated_string = regex.findall(string.lower())
if treated_string == treated_string[::-1]:
    print('Input string %s is a palindrome.' % string)
else:
    print('Input string %s is not a palindrome.' % string)
