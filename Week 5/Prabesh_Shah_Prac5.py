#1
number = input("Enter a number: ")
number = int(number)
print("The number entered was", number)

if (number % 2) == 0:
    print("That is an even number")
else:
    print("That is an odd number")
    
# Enter a number: 12
# The number entered was 12
# That is an even number

# Enter a number: 1
# The number entered was 1
# That is an odd number 

#2
# Get input from the user
number = int(input("Enter a number: "))
# Show the number
print("The number entered was", number)
# Check if num is even or odd
if (number % 2) == 0:
    print("That is an even number")
else:
    print("That is an odd number")
    
    
#3
number = int(input("Enter a number: "))
print("The number entered was", number)
if (number % 2) == 0:
    print("That is an even number")
else:
    print("That is an odd number")

if (number % 10) == 0:
    print("The number is divisible by 10")
else:
    print("The number is not divisible by 10")
    
# Enter a number: 12
# The number entered was 12
# That is an even number
# The number is not divisible by 10

# Enter a number: 100
# The number entered was 100
# That is an even number
# The number is divisible by 10


#4
import sys

count = len(sys.argv)
total = 0

while count > 1:
    count -= 1
    total += float(sys.argv[count])

print("Total is", total)

# Total is 30.0

#5
import sys

count = len(sys.argv)
total = 0

if count > 1:
    while count > 1:
        count -= 1
        total += float(sys.argv[count])

    average = total / (len(sys.argv) - 1)
    print("Total is", total)
    print("Average is", average)
else:
    print("No arguments.")


#6
import sys

# Get the total number of command-line arguments
count = len(sys.argv)
total = 0

# See if arguements were passed
if count > 1:
    # Calculate the total by adding arguments
    while count > 1:
        count -= 1
        total += float(sys.argv[count])

    # Calculate the average
    average = total / (len(sys.argv) - 1)

    # The total and average
    print("Total is", total)
    print("Average is", average)
else:
    # No arguments were provided
    print("No arguments were provided.")

# python total.py 4 8 12

#7
def average(values):
    """Calculates the average of the given list."""
    total = 0
    for n in values:
        # Total the given values
        total += float(n)
    # Return calculated average
    return total / len(values)

# Initialization statement
print("Welcome, utils module has been imported and initialized!")

# Welcome, utils module has been imported and initialized!

#8
import my_utils

average1 = my_utils.average([10, 23, 30])
average2 = my_utils.average([10.2, 8.8, 2.6])

print(average1)
print(average2)

#9
from my_utils import average

average1 = average([10, 23, 30])
average2 = average([10.2, 8.8, 2.6])

print(average1)
print(average2)

#10
import math
dir(math)
# ['__doc__', '__loader__', '__name__', '__package__', 
# '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan',
# 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos',
# 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 
# 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp',
# 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 
# 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 
# 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 
# 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder',
# 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

#11
from import math *
dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', 
#  '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 
#  'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 
#  'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp',
#  'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 
#  'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'math', 'modf',
#  'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh',
#  'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']


#12
import sys

print("The import search path for this program is", sys.path)
# The import search path for this program is ['/path/to/directory', other paths]

#13

IDE
Software for comprehensive coding, debugging, and building.

Module
File containing Python code. Enhances code organization and reusability. Imported using `import` statement.

Command Line Arguments
Values passed to a program during execution. Accessed using `sys.argv` in Python.

Symbol-table
Data structure tracking names (variables, functions) in Python. Accessed with `locals()` and `globals()`.

Search Path
List of directories where Python looks for modules. Stored in `sys.path`. First entry is the script's directory.
