#Assignment3
import string
alphabet = set(string.ascii_lowercase)
def pangram(string):
    return set(string.lower()) >= alphabet
string = input("Enter a string: ")
if(pangram(string) == True):
    print('YES')
else:
    print('NO')
