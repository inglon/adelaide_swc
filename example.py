print 'hello world'
a = 'hello'
c = 5.4
b = 4
d = True
d = False
type(d)
seasons = 4
half = 0.5
seasons + half
seasons/5
seasons/float(5)
> seasons = 4
>>> half = 0.5
>>> seasons + half
4.5
>>> seasons
4
>>> seasons/float(5)
0.8
>>> seasons/5
0
seasons*=4

>>> dna = 'N'
>>> 50*dna
'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN'
>>> dna

dna.upper() #Converts all letters to upper case.
help(str) #q to get out
raw_input()
print 'your name is' + name

a= 'N'
a = a+'N'
a+='N'

'''hjhsdjf a djaio hafha
das hofhsdajkfh  sd''' ###Triple quotes handles string across lines.

file_hanlde.read(3)

>>> file_handle = open('example.fasta', 'r')
os.getcwd()
file_handle.read(3)
file_handle.readlines()
 to_write=open('my_example.txt','w')
>>> to_write.write('Hello I am line\n')
>>>> to_write.close()

c = 'hej'
a = 3
 c+str(a)
'hej3'


 5<=8<100
True
>>> 5<=8>100
False

#Range only work on integers
>>> range(100)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> range(34, 100, 2)
[34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]










>>> my_list = [1,2,3]
>>> len('apples')
6
>>> len(my_list)
3
>>> list1 = [1,2,3]
>>> list2 = [2,3,1]
>>> list1 == list2
False
>>> 'apple'.upper()
'APPLE'
>>> help(str) #list of string methods

>>> #q() to close help()
... 
>>> dir('apple')#list all methods I can use on my string 'apple'
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> combined_string=','.join(['apple','banana','strawberry'])
>>> combined_string
'apple,banana,strawberry'
>>> combined_string.split(',')
['apple', 'banana', 'strawberry']
>>> help('apple'.join)

>>> combined_string
'apple,banana,strawberry'
>>> combined_string.replace('r', 'R')
'apple,banana,stRawbeRRy'
>>> my_list
[1, 2, 3]
>>> dir(my_list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(my_list.append)

>>> my_list.append(4)
>>> my_list
[1, 2, 3, 4]
>>> my_list.append(4)
>>> my_list\
... my_list\
  File "<stdin>", line 2
    my_list\
          ^
SyntaxError: invalid syntax
>>> my_list.count
<built-in method count of list object at 0x7fbcb2c7f8c0>
>>> my_list.count(4)
2
>>> my_list()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>> my_list
[1, 2, 3, 4, 4]
>>> my_list.remove(4)
>>> my_list
[1, 2, 3, 4]
>>> 
>>> my_list.sort()
>>> my_list[0] #Take out first element
1
>>> my_list[1] #Take out second element
2
>>> my_list[0:2] #Up to and not including element 3
[1, 2]
>>> my_list[-1]
4
>>> 

 my_list.reverse()

swc_trainee@swc-bootcamp-007:~/Bootcamp$ python example2.py apple molly
['example2.py', 'apple', 'molly']

import sys
print sys.argv#sys.argv is input variablesimport sys
print sys.argv#sys.argv is input variables


############################
# Sets
############################
>>> 
>>> my_set - set([1,2,3,4,4,4,4,5,6,7])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'my_set' is not defined
>>> my_set = set([1,2,3,4,4,4,4,5,6,7])
>>> my_set
set([1, 2, 3, 4, 5, 6, 7])
>>> my_set = set([1,2,3,4,4,4,4,5,6,7, 'a','d', True])
>>> my_set
set(['a', 1, 2, 3, 4, 5, 6, 7, 'd'])
>>> my_set[0]  #Sets have no order
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
>>> set1 = set([1,2,3])
>>> set2 = set([2,3,4])
>>> dir(set)
['__and__', '__class__', '__cmp__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> set.intersection(set2)
set([2, 3, 4])
>>> #Sets operations are much quicker than list operations.
... 
>>> my_set = set(range(1000))
>>> 985 in my_set
True
>>> 1001 in my_set
False
>>> my_set = set(range(100000))
>>> 20462 in my_set
True
>>> set('apples and bananas')
set(['a', ' ', 'b', 'e', 'd', 'l', 'n', 'p', 's'])
>>> len(set('apples and bananas'))
9
>>> 


isinstance(myobject,str) #This give 
 if not #is the same as if !

##################################
# Dictionaries
##################################
>>> my_dict = {'a':1, 'b':2, 'c':3}
>>> my_dict
{'a': 1, 'c': 3, 'b': 2}
>>> my_dict['b']
2
>>> dir(my_dict)
['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
>>> my_dict.keys()
['a', 'c', 'b']
>>> my_dict.values()
[1, 3, 2]
>>> 
>>> #map integers to words
... 
>>> 'a' in my_dict
True
>>> del my_dict['c']
>>> my_dict
{'a': 1, 'b': 2}
>>> #Keys have to be unique.


def GCcontent(dna):
    dna_noN = dna.replace('N',"")
    Gs = dna_noN.count('G')
    Cs = dna_noN.count('C')
    return (Gs + Cs)/float(len(dna_noN)), len(dna)


##################################
# If, for, while, read line by line
##################################
 number = 10
>>> if number < 100:
...     print 'OK'
... 
OK
>>> 
>>> if number > 0 :
...     print 'OK'
... else number <0: #There is also elif
...     print 'BAD' #Intendention has to be consistent
...

fruits = ['apple','orange','strawberry']
for fruit in fruits:
    print "I am a " + fruit + '.'


fruits = ['apple','orange','strawberry']
for fruit in fruits:
    print fruit, len(fruit)


reader = open('fruit.txt', 'r')
reader
line = reader.readline()
line
print line

while line !='':
    print line
    line = reader.readline()


##################################
# Functions
##################################

def sum_two_numbers(first_number, second_number):
    result = first_number + second_number
    return results

print sum_two_numbers(4, 9)

#Lists and dictionaries will be globally changed if changed
#within the function, even if it is not returned.


##################################
# Classes
##################################


 import rodent
>>> x = rodent.Rodent('A9768',3)
>>> x.capture(2)
>>> x.capture(3)
>>> x.capture(6)
>>> x.capture(6)
>>> x.sighings_per_month
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: Rodent instance has no attribute 'sighings_per_month'
>>> x.sightings_per_month
{2: 1, 3: 1, 6: 2}
>>> rodents['A03867']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'rodents' is not defined
>>> 

#x = filename.classname(arguments)
#x.function()

