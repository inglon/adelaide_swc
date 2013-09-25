#Average pitching for players

#Read the content of the file line by line
reader = open('Pitching.csv','r')
line = reader.readline()
search_me = 'IPOuts'
search_me_index = 0
header_value = line.split(',') #This is a list
for header in header_value:
    if search_me == header:
        break
    search_me_index +=1

#OR simply
#search_me_index = header_values.index(search_me)

line = reader.readline()

IPouts = 0
lines = 0
while line != '':  #line has to exist before this call.
    mylist = line.split(',')
    IPouts=IPouts + float(mylist[search_me_index])
    lines += 1
    line = reader.readline()

print IPouts/float(lines)


