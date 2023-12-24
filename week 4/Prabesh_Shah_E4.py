Functions
Exercises
Week 4

What must be done before a function that is not built-in to Python can be used in a program?
Answer:If you want to use a function that is not built in to python you must either create it yourself and define it with def keyword or import it.
______________________________________________________________________
Given the following import statement, how would a call to the sin() function be made?
import math
Answer:
import math
Angle = math.sin(60)
_________________________________________________________________________
Given the following import statement, how would a call to the sqrt() function be made?
from math import sqrt
Answer:
square_root=sqrt(num)
_________________________________________________________________________
What is the name of the common library that is available with all Python distributions?
Answer:Python Standard Library
_________________________________________________________________________
What keyword is used in Python to define a new function?
Answer:def keyword is used in python to define a new function.
_________________________________________________________________________
Write some Python code that defines a function called print_header(msg). This should
output the value provided by the ‘msg’ parameter to the screen (prefixed by five asterisk
‘*****’) characters.
Answer:
def print_header(msg):
    print("*****", msg)
message = "Hello, World!"
print_header(message)


_________________________________________________________________________
In the answer box below give an example of what the docstring may look like for the
print_header(msg) function.
Answer:
    """ This following function prints five asteriks and hello world."""
    def print_header(msg):
    print("*****", msg)
message = "Hello, World!"
print_header(message)

_________________________________________________________________________
Where within a function definition should a docstring appear?
Answer:
    It should be right below the function defintion as it gives explanation of what the code is about.
_________________________________________________________________________
What statement should appear within a function’s code block to cause a specific value to be
passed back to the caller of the function?
Answer:
    Return statement should be used to return back to caller of function.
_________________________________________________________________________
Write some Python code that defines a function called find_min(a,b) that returns the
smallest of the two given parameter values.
Answer:
    def find_min(a, b):
    return min(a, b)
num = 1
num_2 = 2
result = find_min(num, num_2)
print(f"Smallest num among " {num} and {num_2} is: {result}")

_________________________________________________________________________

Given the following function definition, which of the formal parameters could be described as
being a default argument?
def shouldContinue(prompt, answer=False):
# function body...
Answer:
Paremter answer is the default arguement passed.

Provide two example calls to the above function, one which provides a value for the default
argument, and one that does not.
Answer:
#giving value
shouldContinue("Continue?", True)
#not giving value
shouldContinue("Continue?")

_________________________________________________________________________
State why following function definition would not be allowed.
def do_something(prefix="Message", prompt, answer=False):
# function body...
Answer:
All parameters with default values must come after parameters without default values when designing a 
function with default arguments. This is due to the fact that arguments are assigned values from left to right, 
and if a default argument is encountered, all following parameters must likewise be default parameters.
_________________________________________________________________________
What single character is placed directly before the name of a formal parameter, to indicate
that a variable number of actual parameters can be passed when the function is called?
Answer:
An asterisk (*) is used for *args, allowing a function to accept a variable number of positional arguments.

_________________________________________________________________________
What commonly used built-in function, which displays output on the screen, can take a
variable number of arguments?
Answer:Print() function
_________________________________________________________________________
Is it valid for a function’s parameter name to be prefixed by two asterisk characters ‘**’ as
shown below?

 def send_output(**details):
# function body...
Answer:
Yes it is valird for a function's parameter name to be prefixed by two asterisk.

If present, what does this prefix indicate?
Answer:
It indicates that it will collect any additional keyword arguments passed to the function into a dictionary. 

_________________________________________________________________________
What is the name given to a small ‘anonymous’ function that must be defined using a single
expression?
Answer:
A small 'anonymous' function that must be defined using a single expression is called a "lambda function" in Python. 
Lambda functions are also known as anonymous functions because they don't have a name associated with them. 
They are created using the lambda keyword and are often used for short, simple operations where a full function definition is not necessary. 

Give an example of such a function that calculates the cube of a given number (i.e. the value
of the number raised to the power of three) -
Answer:
cube_num = lambda x: x**3
cube_cube = cube(10)
print(f"The cube of 10 is: {cube_cube}")

_________________________________________________________________________
