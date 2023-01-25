# https://www.programiz.com/python-programming
# Getting Started
print("Hello World")

# Keywords and Identifiers

# False	await	else	import	pass
# None	break	except	in	raise
# True	class	finally	is	return
# and	continue	for	lambda	try
# as	def	from	nonlocal	while
# assert	del	global	not	with
# async	elif	if	or	yield
print(True)
print(False)

# Statement, Indentation and Comments
print('single-line comment: # and multi-line comment: """ """.')

# Variables, Constants and Literals
name = 'Katha Vachhani'
print(name)

list1 = ["apple", "mango", "orange"]
print(list1)

tuple1 = (1, 2, 3)
print(tuple1)

dictionary1 = {'a':'apple', 'b':'ball', 'c':'cat'}
print(dictionary1)

set1 = {'a', 'e', 'i' , 'o', 'u'}
print(set1)

# Data Types
product = ('Microsoft', 'Xbox', 499.99)
print(product[0])
print(product[1])
print(type(product))

capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
print(capital_city['Nepal'])

# Type Conversion and Type Casting
num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))

# Input, Output and Import
print('New Year', 2023, 'See you soon!', sep= '. ') #sep is optional parameter inside the print

x = 5
y = 10
print('The value of x is {} and y is {}'.format(x,y))

# Operators
print("Arithmatic")
a = 10
b = 5
print ('Sum: ', a + b)
print ('Subtraction: ', a - b)
print ('Multiplication: ', a * b)
print ('Division: ', a / b)
print ('Modulo: ', a % b)
print ('Power: ', a ** b)

print("Assignment")
a+=b
print("addition:", a)
a-=b
print("Subtraction:", a)
a*=b
print("Multiplication:", a)
a/=b
print("Division:", a)
a%=b
print("Remainder:", a)
a**=b
print("Exponent:", a)

print("Comparison")
print('a == b =', a == b)
print('a != b =', a != b)
print('a > b =', a > b)
print('a < b =', a < b)
print('a >= b =', a >= b)
print('a <= b =', a <= b)

print("Logical")
print((a > 2) and (b >= 6))
print(True or False)
print(not True)

print("Bitwise")
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)

print("Membership")
dict1 = {1:'a', 2:'b'}
message = 'Hello world'
print('H' in message)
print('hello' not in message)
print(1 in dict1)
print('a' in dict1)

# Namespace and Scope , global local and nonlocal
a = 2
print('id(2) =', id(2))
print('id(a) =', id(a))
def outer_function():
    # global a1
    a1 = 20
    def inner_function():
        a1 = 30
        print('a1 =', a1)
    inner_function()
    print('a1 =', a1)
a1 = 10
outer_function()
print('a1 =', a1)

# if...else Statement
if a > 0:
    print('Positive number')
else:
    print('Negative number')

if b > 0:
    print("Positive number")

elif b == 0:
    print('Zero')
else:
    print('Negative number')

number = 0
if (number >= 0):
    # inner if statement
    if number == 0:
        print('Number is 0')
    # inner else statement
    print("number is positive")
else:
    print('Number is negative')

# for Loop
testing = ['manual', 'api', 'automation', 'performance']
for types in testing:
    print(types)
for i in range(0,5):
    print(i)

# while Loop
count = 0
while count < 4:
    print("inside the loop")
    count = count + 1
    print(count)
# break and continue
for i in range(5):
    if i == 3:
        break
    print(i)

print("Odd Number")
num = 0
while num < 10:
    num += 1
    if (num % 2) == 0:
        continue
    print(num)

# pass statement
n = 9
if n > 10:
    pass
print('Hello')

# Functions
# Function Arguments
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name = 'Vachhani', first_name = 'Katha')

# Global Keyword
c = 1
def add():
    # use of global keyword
    global c
    c = c + 2
    print(c)
add()

# Modules
import math
# use math.pi to get value of pi
print("The value of pi is", math.pi)

# Directory and Files Management
# file = open('Data.txt')
# readFile = file.read()
# print(readFile)

