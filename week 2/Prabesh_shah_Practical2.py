#1
total = 100
print("The total is", total)
#The total is 100

#2
total = total + 99
print("The total is now", total)
#the total is 199

#3 
total -= 1
print("The total is", total)
total *= 4
print("The total is", total)
total /=2
print("The total is", total)

#4
total = 98.2
count = 5
average = total / count
print(f"Average: {average}")
#Average: 19.64

#5
print(type(False))
print(type(1000))
print(type(100.111))
print(type("Hello"))
print(type(True))
print(type(100 / 5))
print(type(100 // 5))
# <class 'bool'>
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>
# <class 'float'>
# <class 'int'>

#6
print("ABC" * 10)
#ABCABCABCABCABCABCABCABCABCABC

#7
name = "Prabesh Shah"
address = "Biratnagr,Tribhuvanchowk,Morang"
contact = "9863889066"

print("Name:", name)
print("Address:", address)
print("Contact:", contact)
print("Length:", len(name))
# Name: Prabesh Shah
# Address: Biratnagar,Tribhuvanchowk,Morang
# Contact: 091234
# Length: 12

#8
age = input("Enter your age ")
print("in one year your age will be", age + 1)
#The following program doesnt work as input() usually takes the values as a string and string and int cant be added.

#9
num1 = int(input("Enter a num: "))
num2 = int(input("Enter a num: "))
product = num1 * num2
print(f"The product of {num1} and {num2} is: {product}")
# Enter a num: 12
# Enter a num: 3
# The product of 12 and 3 is: 36

#10
comment = "I would have "thought" you knew better!"
#Syntax error will be shown if you use "" as string delimiter since it has already been used inside with thought.

#11
print('This text includes characters such as \\\' \\" and \\\'\',\nThis is a new line that starts with a tab\n\tThis new line starts with two tabs')
#This text includes characters such as \' \" and \'',
# This is a new line that starts with a tab
# 	This new line starts with two tabs 

#12
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("Hello there!")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Hello there!
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
#13
print("""
This text spans three lines,
and includes both single ('),
and double quotes (").
""")
#This text spans three lines,
# and includes both single ('),
# and double quotes (").

#14
surname = "Palin"
initial = surname[2]
print("The third letter of the surname is:", initial)
#The third letter of the surname is: l

#15
surname = "Palindranath"
initial = surname[9]
print("The tenth letter of the surname is:", initial)
#The tenth letter of the surname is: a

#16
surname = "Palindranath"
initial = surname[-2]
print("The second letter of the surname from last is:", initial)
#The he second letter of the surname from last is: t

#17
surname = "Palin"
surname_slice = surname[1:]
print("Surname:", surname_slice)
#Surname:alin

#18
surname = "Palin"
surname_slice = surname[0:4]
print("Surname:", surname_slice)
#Surname:Pali

#19
primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
four_primes = primes[0:4]
print("The first four prime numbers:", four_primes)
# The first four prime numbers: [2, 3, 5, 7]

#20
names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
name1 = "Ram"
name2 = "Bahadur"
names[6:6] = [name1, name2]
print("List :", names)
#List : ['Terry', 'John', 'Michael', 'Eric', 'Terry', 'Graham', 'Ram', 'Bahadur']

#21
nums = [1,2,3] * 5
print(nums)
#[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

#22
# In programming, assignment is the process of assigning a value to a variable. 

# A data-type is a classification of data, such as integer, float, string, etc.
# Each data-type can hold different types of values. 

# An argument is a value that is passed into a function.

# Indexing is the process of accessing an element from a data structure, such as a list 
# or a string, by specifying its position.

# Slicing is the process of extracting a subsequence from a sequence, such as a list or a string.

# A mutable data type is a data type whose state or value can be changed after it is created.

# An immutable data type is a data type whose state or value cannot be changed after it is created. 