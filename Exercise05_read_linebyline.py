#Read the content of the file line by line
reader = open('pg76.txt','r')
#line = reader.readline()

length = 0
lines = 0
while line != '':  #line has to exist before this call.
    length=length + len(line)
    lines += 1
    line = reader.readline()
   
print length 
print lines 
print 'Total length: %d, line count: %d' %(length, lines)

#Get the length of each line and aggregate it
#Get the total number of lines in a file


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



