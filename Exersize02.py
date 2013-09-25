#Number of unique letters in a string

#Read string
import sys
mystring = sys.argv[1:]
mystring = ''.join(mystring)
mystring.replace(',','') #Replace the commas with nothing
mystring.remove(',')
mystring.remove('.')
#This would be best
all_permitted_letters = 'abcdefghijklmnopqrstuvwxyz'
mystring = mystring.intersection(all_permitted_letters)

#Transform all to capitals
mystring = mystring.upper()

#Transform to a set
myset = set(mystring)

#Count length
out = len(myset)

#Print
print out
