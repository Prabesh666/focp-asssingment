#1
import math

squares = [1, 4, 9, 16, 25]
for square in squares:
    root = math.sqrt(square)
    print(root)
# 1.0
# 2.0
# 3.0
# 4.0
# 5.0

#2
squares = [1, 4, 9, 16, 25]
squares.append(49)
squares.append(64)
squares.append(81)
print(squares)
# [1, 4, 9, 16, 25, 49, 64, 81]

#3
squares.extend([121, 144, 169])
print(squares)
# [1, 4, 9, 16, 25, 121, 144, 169]

#4
squares.insert(0, 2)
print(squares)
# [2, 1, 4, 9, 16, 25]

#5
squares = [1, 4, 9, 16, 25,44,49]
squares.remove(49)
print(squares)
# [1, 4, 9, 16, 25, 44]

#6
squares = [1, 4, 9, 16, 25]
squares.remove(3)
print(squares)
# ValueError: list.remove(x): x not in list

#7
squares = [1, 2, 3, 1, 2]
squares.remove(2)
print(squares)
# [1, 3, 1, 2]

#8
squares = [1, 4, 9, 16, 25]

last_value = squares[-1]
print("Last value of the list: ", last_value)
squares.remove(last_value)
print("The updated list is:", squares)
# Last value of the list:  25
# The updated list is: [1, 4, 9, 16]

#9
squares = [1, 4, 9, 16, 25]
first_value = squares.pop(0)
print("The first value of the list is:", first_value)
print("The updated list is:", squares)
# The first value of the list is: 1
# The updated list is: [4, 9, 16, 25]

#10
names.sort()
print("The sorted list is:", names)
# The sorted list is: ['Eric', 'Sophie', 'anna', 'sam']

#11
names = [ "Eric", "anna", "Sophie", "sam"]
names.sort(key=lambda x: x.upper())
print("The sorted list is:", names)
# The sorted list is: ['anna', 'Eric', 'sam', 'Sophie']

#12
squares = [1, 4, 9, 16, 25]
squares.reverse()
print("The reversed list is:", squares)
# The reversed list is: [25, 16, 9, 4, 1]

#13
colours = ["red", "green", "yellow", "blue", "red"]
print(colours.index("blue"))
#3

#14
colours = ["red", "green", "yellow", "blue", "red"]
colours_copy = colours.copy()

print("Original list: ", colours)
colours[0] = "black"
colours[1] = "white"

print("Modified original list: ", colours)
print("Copy: ", colours_copy)
# Original list:  ['red', 'green', 'yellow', 'blue', 'red']
# Modified original list:  ['black', 'white', 'yellow', 'blue', 'red']
# Copy:  ['red', 'green', 'yellow', 'blue', 'red']

#15
cubes = [x ** 3 for x in range(2, 21)]
print("Cubes of numbers:")
# Cubes of numbers: [8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331,
# 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000]

#16
# The some_users list comprehension will contain the user names from 
# the all_users list where the length of the user name is less than 8.
# The condition that has to be met for inclusion is the length of the
# user name. Only those user names with a length less than 8 will be
# added to the some_users list.

#17
address = ("1819", "Lagankel,Lalitpur", "H123")
print(address)
# ('1819', 'Lagankhel,Lalitpur', 'H123')

#18
address = ("1819", "Lagankhel,Lalitpur", "H123")
print(type(address))
# <class 'tuple'>

#19
address = ("1819", "Lagankhel,Lalitpur", "H123")
ghar_no, ward_no, postcode = address
print(address)
print(type(ghar_no))
# ('1819', 'Lagankhel,Lalitpur', 'H123')
# <class 'str'>

#20 
address = ("1819", "Lagankhel,Lalitpur", "H123")
print(*address)
# 1819 Lagankhel,Lalitpur H123

#21
# Method: Function associated with objects in OOP.
# List Comprehension:cConcise list creation in Python.
# Tuple:cImmutable, ordered collection in parentheses.
# Tuple Packing:cImplicitly creating a tuple from values.
# Sequence Unpacking: Extracting values from a sequence into variables.

