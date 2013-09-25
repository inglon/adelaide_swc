#Import variables
import sys
wordlist = sys.argv
wordlist = wordlist[1:]#to is missing so takes all
                       #Take away 

#Sort variables
wordlist.sort()

#Join all except the last string by ','
l=len(wordlist)
sorted1 = wordlist[0:(l-1)]
sorted1=','.join(sorted1)

#Put the last bit of the sentence at the end.
sorted12=', and '.join([sorted1,wordlist[l-1]])
#OR sorted12 += ',and' + word[-1] + '.'

#Capitalize the first letter
sorted1 = sorted1.title()
#OR use capitalize or index the string with [...]

print sorted12


#[0:-1] takes all elements up to the last but not including the last
