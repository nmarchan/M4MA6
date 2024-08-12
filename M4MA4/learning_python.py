lp = open("learning_python.txt", 'r') #object for learning_python.txt file"

print(lp.read()) #print entire file

lp.seek(0) #returns to start of file

for i in lp:
    print(i, end='') #end line characters already exist in file
    
lp.seek(0)

textlines = [] #blank list for lines of text read from file

for line in lp:
    textlines.append(line) #add line to list
for x in textlines:
    print(x, end='') #print from list

for y in textlines: #Replace Python with PHP and print
    print(y.replace('Python', 'PHP'), end='')

lp.close() #closing file
