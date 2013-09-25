#Take genome string
#Output dictionary with A: # As in stings, B:...

#Input string
input_string = 'GAGAGATGATGCGCGCGCGCGCCCCTTTAA'
As = input_string.count('A')
Ts = input_string.count('T')
Cs = input_string.count('C')
Gs = input_string.count('G')

my_dict = {'A':As, 'T':Ts, 'C':Cs, 'G':Gs}
gc_cont = (Gs+Cs)/float(len(input_string))
#OR my_dict['G'] + my_dict['C']...

print my_dict
print gc_cont
