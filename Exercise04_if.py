import sys
number = sys.argv[1]
number = int(number) #Convert the string to integer

if number % 5  >0:
    print 'EVEN'
else:
    print 'ODD'


