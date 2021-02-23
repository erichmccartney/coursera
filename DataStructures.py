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

#/ Assignment 6.5 

#Write code using find() and string slicing (see section 6.10) 
#to extract the number at the end of the line below. Convert the 
#extracted value to a floating point number and print it out./#

text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('.')
print(float(text[pos-1:pos+5]))