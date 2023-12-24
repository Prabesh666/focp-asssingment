#1
import math
number = 2401
num_sqrt = math.sqrt(number)
print(f"The square root of {number} is: {num_sqrt}")

#2
from math import log2

number = 1024
log_base = log2(number)

print(f"The log base 2 of {number} is: {log_base}")

#3
from math import log2

def calc_log_base(value):
    return log2(value)
num_calls = [256, 512, 1024]

for num in num_calls:
    result = calc_log_base(num)
    print(f"The log base 2 of {num} is: {result}")

#4
from math import log2

def calc_log_base(num):
    """
    Calculate the logarithm base 2 of the given value.
    This function takes a numerical value as input and returns log base 2
    of that value using the log2 function from the math module.
    """
    return log2(num)


num_calls = [256, 512, 1024]

for num in num_calls:
    result = calc_log_base(num)
    print(f"The log base 2 of {num} is: {result}")

help(calc_log_base)

#5
def multiply_values(num1, num2=0):
    if num2 == 0:
        return num1 * num1
    else:
        return num1 * num2

multi_1 = multiply_values(2,3)
multi_2 = multiply_values(4)

print(f"Two passed arguements: {multi_1}")
print(f"Same argument multiply: {multi_2}")

#6
def multiply_values(num1, num2=0):
    if num2 == 0:
        return num1 * num1
    else:
        return num1 * num2
        
multi_1 = multiply_values(num1=2,num2=3)
multi_2 = multiply_values(num1=4)

print(f"Two passed arguements: {multi_1}")
print(f"Same argument multiply: {multi_2}")

#7
print("a","b","c","d" ,end=" ")
print("a","b","c","d" ,end="\n")
print(1,2,3,4, sep=",")

#8
def calc_avg(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

output1 = calc_avg(1, 2, 3, 4, 5)
output2 = calc_avg(10, 20, 30)

print(f"Average : {output1}")
print(f"Average : {output2}")

#9
import math

hypot = lambda a, b: math.sqrt(a * a + b * b)
result = hypot(3, 4)
print(result)
print(type(hypot))

#10
to_seconds = lambda hours, minutes: hours * 3600 + minutes * 60

result1 = to_seconds(1, 30)  
result2 = to_seconds(2,0)  

print(f"Total seconds : {result1} seconds")
print(f"Total seconds : {result2} seconds")

#11
to_seconds = lambda hours, minutes=0: hours * 3600 + minutes * 60

result1 = to_seconds(1, 30)
result2 = to_seconds(2)    

print(f"Total seconds : {result1} seconds")
print(f"Total seconds : {result2} seconds")

