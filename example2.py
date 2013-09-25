#Day 2

######################################
# Testing
######################################

def dna_starts_with(sequence, tag):
    length = len(tag)
    return sequence[0:length] == tag


#Test the function with assert
assert dna_starts_with('a','a')
    #Will be silent if True and hence correct
assert not dna_starts_with('at','ta')
    #Will be silent if False and hence correct

#Test several things via table
#Sequence Prefix Expected
Tests = [
['a','a',True],
['at', 'ta', False]
]
passes = 0
for (seq, prefix, expected) in Tests:
    if dna_starts_with(seq, prefix) == expected:
        passes += 1
print '%d/%d tests passed' %(passes, len(Tests))

#OR better
passes = 0
for (i, (seq, prefix, expected)) in enumerate(Tests):
    if dna_starts_with(seq, prefix) == expected:
        passes += 1
    else:
        print('test %d failed' % i)
print '%d/%d tests passed' %(passes, len(Tests))



def nucleotideContent(dnaString):    
    '''This function must return the contribution    
    of nucleotides ATCG (as uppercase) from a given DNA     
    string inside a dictionary, where each key refers to    
    a nucleotide    
    '''    
    dnaDict = {}    
    uniques=set(dnaString)    
    for nucleotide in uniques:    
        dnaDict[nucleotide]=dnaString.count(nucleotide)        
    return dnaDict

Tests = [['ACGTGT',{'A':1, 'C':1, 'G':2,'T':2}],
['CAGGTT', {'A':1, 'C':1, 'G':2,'T':2}]]

passes = 0
for (i, (seq, expected)) in enumerate(Tests):
    #enumerate returns and index and the object with that index
    #so the (i, (seq, expected)) is the enumerate format, not to do with for
    if nucleotideContent(seq) == expected:
        passes +=1
    else:
        print('test %d failed' %i)
print '%d/%d tests passed' %(passes, len(Tests))

#####################################################
# Slicing
#####################################################
s = 'hejja'
#Slice with [start:end:stepsize]

s[::2]
s[::-1]
s[3:5:-1]



#####################################################
# Nosetests
#####################################################
#Testing with nosetest, see file test_dna_starts.py
#That puts all tests for a functio in the same file.    

#####################################################
# Doctests
#####################################################

#This package has testing within each function

def factorial(n):
    '''Return the factoral of n, an
    integer >= 0
    >>> factorial(4)
    24
    '''
    import math
    if not n >=0:
        raise ValueError('n must be >= 0')
    if math.floor(n) != n:
        raise ValueError('n must be an integer')
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()

#This doctest will evaluate factorial(4) and complain if not equal 
#to 24.
#Run a script with myscript.py -v will give an OK output
#rather than silent for OK.

#####################################################
# Error handling
#####################################################

#This helps me see if this error was one that I expected someone
#might do, or if this is something I had no idea would happen.

try:
    mystatement1
    mystatement2
    ...
except IOError as err:
    print err.message
except ValueError as err:
    print err.message


#dir(IOError) will tell me what I get get from err

try:
    grid = read_grid(whatever)    
except IOError:
    grid = defaul_grid()


#####################################################
# Error handling, exception classes
#####################################################

class UnknownBaseException(Exception)
    pass

def dna_starts_with(sequence, tag):
    if len(tag)>len(sequence)
        raise Exception('string 2 is longer than string 1')
    length = len(tag)
    return sequence[0:length] == tag

#OR use
    try:
        dna_starts_with('N', 'a')
    except UnknownBaseException() as e: print 'contains N'  

    if 'N' in sequence:
#   raise Exception('containts invalid bases')
    raise unknownBaseException()       


#####################################################
# Version control
#####################################################
#Git, a version control system
#See etherpad.


