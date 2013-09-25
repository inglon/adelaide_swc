
#Given the string 'dna', replace all 'N', return the GC-content

def GCcontent(dna):
    dna_noN = dna.replace('N',"")
    Gs = dna_noN.count('G')
    Cs = dna_noN.count('C')
    return (Gs + Cs)/float(len(dna_noN)), len(dna)

def GCcontent(dna):
    dna_noN = dna.replace('N',"")
    Gs = dna_noN.count('G')
    Cs = dna_noN.count('C')
    return (Gs + Cs)/float(len(dna_noN))


def Ncontent(dna):
    Ns = dna.count('N')
    return (Ns)/float(len(dna))


def sum_two_numbers(first_number, second_number):
    result = first_number + second_number
    return results

print sum_two_numbers(4, 9)

dna = 'AGCTNNCTC'
gc, length_dna = GCcontent(dna)


def change_list(a_list, to_change = 'I changed this!'):
    a_list[0] = to_change


a = [1,2,3,4]
change_list(list(a))
print a

#Exercise 2
Sequence 1
ATGGGGGTGTGTGNNNNNNTGA
Sequence 2
ATGCCCGCGCGCGCTGA
Sequence 3
GGGTGGTGTGTGACAAAAAAAA

#Give a string 'filename', write a function which opens the file, iterates over all sequences, and writes a bit of stats about each sequence:

-Name of each sequence ('Sequence 1', ...)
-Counts of Ns
-GC-content

Print number of sequences in that file.

example_fasta = 'Fasta_examples.txt'
def give_stats(example_fasta):
    #Read/open the file
    reader = open(example_fasta,'r')
    line = reader.readline()
    my_dict = {}
    while line != '':  #line has to exist before this call.
        if line.startswith('>')
            name = line.lstrip('>').rstrip('\n')
        else:
          my_dict[name] = [GCcontent(line), Ncontent(line)])    
    line = reader.readline()

    #For each line in the file, save name, nNs, GC

    



