#Test file
#Test boundary cases that are completely different
#In this script we use doctest instead of nosetest

def dna_starts_with(sequence, tag):
    '''Check if sequence starts with tag
    >>> dna_starts_with('acgtgtcgat', 'acgtgtcgat')
    True
    >>> dna_starts_with('cgtgc', 'c')
    True
    >>> dna_starts_with('acgtgtcgat', 'acgtgtcgatacgtgtcgat')
    False
    '''

    length = len(tag)
    return sequence[0:length] == tag

if __name__ == '__main__':
    import doctest
    doctest.testmod()

