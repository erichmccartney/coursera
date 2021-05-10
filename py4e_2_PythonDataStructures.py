# Chapter 6 - Strings

fruit = 'banana'
letter = fruit[1]
print(letter)

x = 3
w = fruit[x-1]
print(w)

zot = 'abc'
print(zon[5])

fruit = 'banana'
x = len(fruit) #LEN asks for the length of a string
print(x)

#Print every letter in fruit word
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

#Print with for loop this time
fruit = 'banana'
for letter in fruit :
    print(letter)

#Count number of a's in banana
word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
    print(count)

#Slicing
s = 'Monty Python'
print(s[0:4])

print(s[6:7])

print(s[6:20]) #ok to reference beyond end of string

print(s[:2])
print(s[8:])
print(s[:])

#Manipulating Strings
#Sting Methods  https://docs.python.org/3/library/stdtypes.html#string-methods
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())

stuff = 'Hello World'
type(stuff)
<class 'str'>
dir(stuff)

fruit = 'banana'
pos = fruit.find('na')
print(pos)

pos = fruit.find('z') #can't find it returns a -1
print(pos)

#Quiz Chapter 6

#Q3
x = 'From marquard@uct.ac.za'
print(x[8])

#Q4
x = 'From marquard@uct.ac.za'
print(x[14:17])

#Q6
print(len('banana')*7)

#Q7
greet = 'Hello Bob'
print(greet.upper())

#Q9
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

#/ Assignment 7.2 

#/Write a program that prompts for a file name, then opens that 
#file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each
#of the lines and compute the average of those values and produce 
#an output as shown below. Do not use the sum() function or a variable 
#named sum in your solution.
#You can download the sample data at 
#http://www.py4e.com/code3/mbox-short.txtWrite 

# Use the file name mbox-short.txt as the file name
def getValue(sLine):
    c = sLine.find(':')
    return float(sLine[c+1:])

fname = input("Enter file name: ")
fh = open(fname)
fSum = 0
nCount = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    fValue = getValue(line)
    fSum = fSum + fValue
    nCount = nCount + 1

#print ("Each:", fValue, fSum, nCount)
print("Average spam confidence:", fSum/nCount)

# Chapter 8 - Lists

# 8.2 Manipulating Lists

# Method 1 - only keeps 1 number in memory
total = 0
count = 0
while true :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average: ', average)

# Method 2 - keeps numbers in memory
numlist = list()
while true :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average: ', average)

# 8.3 Lists and Strings

# Split
abc = 'With three words'
stuff = abc.split() #convert string to list
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff :
    print(w)

line = 'A lot     of spaces'
etc = line.split() #extra spaces still work
print(etc)

line = 'first;second;thrid'
thing = line.split()    #default only recognizes space delimiter
print(thing)
print(len(thing))

thing = line.split(';') #specify delimiter
print(thing)
print(len(thing))

# Strip

# Example Data Line from txt file
# From stephen.marqurd@uct.ac.za Sat Jan 5 09:14:16 2008

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue  #skip lines w/o 'from '
    words = line.split()    #chop by spaces
    print(words[2]) #second word is 'Sat'

# Double Split

words = line.split()
email = words[1]    #pulls 'stephen.marqurd@uct.ac.za'
pieces = email.split('@')
print(pieces[1])    #pulls ' uct.ac.za'


# Quiz Chapter 8

#Q3 
friends = [ 'Joseph', 'Glenn', 'Sally' ]
print(friends[2])

#Q4
fruit = 'Banana'
fruit[0] = 'b'  #trick code, does nothing
print(fruit)    #prints 'banana'

#Q6
x = list(range(5))

#Q7
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))

#Q7
t = [9, 41, 12, 3, 74, 15]
t[2:4]  #prints [12, 3]

#Q10
friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])

#/ Assignment 8.4 
#
#Open the file romeo.txt and read it line by line. 
#For each line, split the line into a list of words using the split() 
#method. The program should build a list of words. For each word on 
#each line check to see if the word is already in the list and if not 
#append it to the list. When the program completes, sort and print the 
#resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt /#

fname= input('Enter a file name: ')
fh = open(fname)
lst = list()                      
for line in fh:                   
    word = line.split()    
    for element in word:          
        if element not in lst:         
            lst.append(element)  
print(sorted(lst))

#/ Assignment 8.5 Open the file mbox-short.txt and read it line by line. 
#When you find a line that starts with 'From ' like the following line:
#
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
#You will parse the From line using split() and print out the second word 
#in the line (i.e. the entire address of the person who sent the message). 
#Then print out a count at the end.
#
#Hint: make sure not to include the lines that start with 'From:'. 
#Also look at the last line of the sample output to see how to print the 
#count.
#
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
/#

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : continue  #skip lines w/o 'from '
    email = line.split()   #chop by spaces
    count = count + 1
    print(email[1]) #pull email

print("There were", count, "lines in the file with From as the first word")

###############################################################
############### Chapter 9 - Dictionaries ######################
###############################################################

# Lists index their entries based on the postion in the list
# Dictionariesa re like bages - no order

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

jjj = { 'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(jjj)
ooo = { }
print(ooo)

# 9.2 Counting with Dictionaries

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)
'csev' in ccc

counts = dict()
names = ['csev', 'cwen', 'zqian', 'cwen']
for name in names :
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

# Get Method

if name in counts:
    x = counts[name]
else :
    x = 0

x = counts.get(name, 0)
print(x)

# Simplified Counting with get()

counts = dict()
names = ['csev', 'cwen', 'zqian', 'cwen', 'csev']
for name in names : 
    counts[name] = counts.get(name, 0) + 1
print(counts)

# 9.3 Dictionaries and Files

