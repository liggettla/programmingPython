#This needs to be run in python 3

mystr = 'xxxSPAMxxx'
#returns 3 which is the offset of SPAM in the string
mystr.find('SPAM')
mystring = 'xxaaxxaa'

#this replaces all instances of 'aa' with 'SPAM' and creates a new string, but cannot change the old string because strings are immutable
mystring.replace('aa', 'SPAM')
'SPAM' in mystring
mystr = '\t Ni\n'
#This removes both the '\t' and the '\n'
mystr.strip()
#This only removes the '\n' from the right side of the string
mystr.rstrip()
#Changes to lowercase
mystr.lower()
#Returns True if it is a string of letters
mystr.isalpha()
#Returns True if it is a string of numbers
mystr.isdigit()

import string
#prints all possible ascii characters
print(string.ascii_lowercase + '\n')
string.whitespace + '\n'

print('String Splitting\n')
delim = 'NI'
print(delim.join(['aaa', 'bbb', 'ccc']) + '\n')
print(' '.join(['A', 'dead', 'parrot']) + '\n')
#convert string to char list
chars = list('Lorreta')
print(chars)
chars.append('!')
print(''.join(chars))
#same function as str.replace() the hard way
mystr = 'xxaaxxaa'
print('SPAM'.join(mystr.split('aa')))
#type conversions
print('\nType Conversions')
x = int('42')
y = eval('42')
print(x, y)
x = str(42)
y = repr(42)
print(x, y)
print('42' + str(1), int('42') + 1)
print('%d' % 42, '{:d}'.format(42))

