#Number of union and intersect letters in two strings
string1 = 'A very, very important sentence'
string2 = 'Another sentence that is less important'

#Read string
string1 = string1.lower()
letters2 = set(string1)
all_permitted_letters = set('abcdefghijklmnopqrstuvwxyz')
mystring = string1.intersection(all_permitted_letters)

string2 = string2.lower()
letters = set(string2)
letters2 = string2.intersection(all_permitted_letters)

in_common = len(string)

#Transform all to capitals
mystring = mystring.upper()

#Transform to a set
myset = set(mystring)

#Count length
out = len(myset)

#Print
print out
