#1
print(10 < 100)
print(100 != 100)
print(50 >= 50)
# True
# False
# True

#2
age = 19
if age ==19 :
    print("Age is 19 ")
elif age < 20:
    print("Age is smaller than 20")
else:
    print("Age is smaller than 31")
#Age is 19

#3
print("a" < "b")

print("b" < "a")

print("John" < "Terry")
# True
# False
# True

#4
print("john" < "Terry")
print([1,2,3] < [1,2,3])
print([1,2,2] < [1,2,3])
# False
# False
# True

#5
print(5 < 10.2)
print(5 < "Monty")
print(5 < "5")
# True
# TypeError: '<' not supported between instances of 'int' and 'str'

#6
age = 30
first_condition = age >= 18 and age <= 65
print("Age between 18 and 65:", first_condition)
second_condition = age < 18 or age > 65
print("Age less than 18 or greater than 65:", second_condition)
third_condition = not age > 18
print("Age not greater than 18:", third_condition)
# Age between 18 and 65: True
# Age less than 18 or greater than 65: False
# Age not greater than 18: False


#7
age = 30
result = (age >= 18 and age <= 65) and (not age == 30)
print(result)
#False

#8
weight = 58
height = 178
condition1 = 100 < weight < 200
condition2 = 131 < height < 160
print(condition1)
print(condition2)
#False
#False

#9
names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
result1 = "Prasi" in names
print(result1)
result2 = "John" not in names
print(result2)
message = "Hello there, my name is John"
result3 = "world" in message
print(result3)
result4 = "my name is" not in message
print(result4)
# False
# False
# False
# False

#10
age = 19 
if 18 <= age <= 30:
    print("You are still young.")
else:
    print("You are old.")
#You are still young.

#11
age=19
if 18 <= age <= 30:
    print("You are still young!")
elif 30 < age <= 40:
    print("You are in your 30s.")
else:
    print("You are Old.")
#You are still young.

#12
name = input("Enter your name: ")
if len(name) == 0:
	print("Please enter your name.")
else:
    print("Your name is:",name)
#if you enter a name else condition is executed if you dont enter anything first condition is exectued.

#13
age=19
print("you are an adult") if age >= 18 else print("you are not an adult, yet!")
#you are an adult

#14
names = ["Denzi", "Sakar", "Prasi", "Perlex"]
for name in names:
    print(name)
# Denzi
# Sakar
# Prasi
# Perlex

#15
for i in range(2, 11, 2):
#range(2, 11, 2) generates values from 2 to 10 with a step of 2.
    result = i ** i
    print(f"{i} to the power of {i} = {result}")
# 2 to the power of 2 = 4
# 4 to the power of 4 = 256
# 6 to the power of 6 = 46656
# 8 to the power of 8 = 16777216
# 10 to the power of 10 = 10000000000

#16
numbers = [10, 20, 30, 90, 200, 30, 22, 11]
total = 0
for num in numbers:
    total += num
    print(f"Total: {total}")
# Total: 10
# Total: 30
# Total: 60
# Total: 150
# Total: 350
# Total: 380
# Total: 402
# Total: 413

#17
numbers = [10, 20, 30, 90, 200, 30, 22, 11]
total = 0
for num in numbers:
    total += num
    print(f"Total: {total}")
    if total > 100:
        print("Exceeded 100.")
        break
# Total: 10
# Total: 30
# Total: 60
# Total: 150
# Exceeded 100.

#18
numbers = [10, 20, 30, 90, 200, 30, 22, 11]
total = 0
for num in numbers:
    total += num
    print(f"Total: {total}")
    if total >= 100:
        print("Exceeded 100.")
else:
    print("All numbers are processed.")
# Total: 10
# Total: 30
# Total: 60
# Total: 150
# Exceeded 100.
# Total: 350
# Exceeded 100.
# Total: 380
# Exceeded 100.
# Total: 402
# Exceeded 100.
# Total: 413
# Exceeded 100.
# All numbers are processed.

#19
# A Boolean expression is an expression that evaluates to either True or False.

# Relational operators are used to compare two values and determine the relationship between them.

# Logical operators perform logical operations on Boolean values.

# Operator chaining refers to the ability to use multiple operators in a single expression.

# The ternary operator is a concise way to write an if-else statement in a single line.

# Iteration is the process of repeatedly executing a block of code.

# A nested loop is a loop inside another loop.


