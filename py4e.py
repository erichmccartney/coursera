help("keywords")


#Week 4
#Chapter 2
#Assignment 2.2
name = input("Enter your name")
print("Hello", name)

#Assignment 2.3
hrs = float(input("Enter Hours:"))
rate = float(input("Enter Hourly Rate:"))
pay = hrs * rate
print("Pay:", pay)

#Exercise 2.3
xh = float(input("Enter Hours: "))
xr = float(input("Enter Rate: "))
xp = xh *xr
print("Pay:",xp)

#Chapter 3.1
x = 5
if x < 10:
    print('Smaller') #indent has a syntax to the operation
if x > 20:
    print('Bigger')
print('Finis')

#Example Continued to demonstrate indent syntax
#Tab should equal 4 spaces or Python gets confused
print('Before 5')
if x ==5 :
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
print('Afterwards 5')
print('before 6')
if x == 6 :
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
print('Afterwards 6')

#Example continued
for i in range(5) :
    print(i)
    if i > 2 :
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')

#Nested Decisions
x = 42
if x > 1 :
    print('More than one')
    if x < 100 :
        print('Less than 100')
print('All done')

# Two-way decisions
x = 2
if x > 2 :
    print('Bigger')
else :
    print('Smaller')
print('All Done')

#Chapter 3.2
#elif example
x= 10
if x < 2 :
    print('small')
elif x < 10 :
    print('medium')
else :
    print('LARGE')
print('All Done')

# Traceback - Try and Except Example

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print ('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print ('Second', istr)

#Quiz Chapter 3

#Problem 3
x = 5
if  x == 5 :
    print('Is 5')
    print('Is Still 5')
    print('Third 5')

#Problem 7
x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')

#Problem 9
astr = 'Hello Bob'
istr = int(astr)
print('First', istr)
astr = '123'
istr = int(astr)
print('Second', istr)

#Problem 10
astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
print(istr)

# Assignment 3.1
fh = float(input("Enter Hours:"))
fr = float(input("Enter Rate:"))

if fh <= 40 :
    pay = fh * fr
else :
    pay = (40 * fr) + ((fh - 40) * (1.5 * fr))
print('Pay:', pay)

# Assignment 3.3

score = input("Enter Score: ")

try:
    sc = float(score)
except:
    print('Error, please enter a number')
    quit()

if sc  >= 1.0 or sc <= 0.0 :
    print('Error, out of range. enter number between 0.0 and 1.0')
    quit()

if sc >= 0.9 :
    print('A')
elif sc >= 0.8 :
    print('B')
elif sc >= 0.7 :
    print('C')
elif sc >= 0.6 :
    print('D')
elif sc < 0.6 :
    print('F')