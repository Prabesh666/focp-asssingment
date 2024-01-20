I/O and File Handling
Exercises
Week 8

Which of the following represents a Python f-string?
a) "Hello {}, you have logged in".format(name)
b) "Hello {name}, you have logged in"
c) f"Hello {name}, you have logged in"
d) "Hello %s, you have logged in" % name
Answer:c
_________________________________________________________________________
Given the following definition of value, what would each of the following statements
display?
value = 10.768572
print(f"Value is {value}")
Answer: Value is 10.768572

print(f"Value is {value * 10}")
Answer: Value is 107.68572
    
print(f"Value is {value:.2f}")
Answer: Value is 10.76
    
print(f"Value is {value:16.2f}")
Answer:Value is 10.77

print(f"Value is {value:0>16.2f}")
Answer:Value is 0000000000010.77
_________________________________________________________________________
Within an f-string format specifier what does the ‘^’ alignment character signify?
Answer:The caret (^) in an f-string format specifier means center alignment.
_________________________________________________________________________
Write a statement which uses the str.format() to generate the same output as the
following f-string statement -
print(f"pi to 5 decimal places is {math.pi:.5f}")
Answer:print("pi to 5 decimal places is {:.5f}".format(math.pi))

________________________________________________________________________
What would the following statement display?
print("Length = {1} Width = {0}".format(10,20))
Answer:Length = 20 Width = 10
_________________________________________________________________________
What exactly would the following statement display?
print("Hello".rjust(10))
Answer:     Hello

_________________________________________________________________________
On which older programming language is the %-formatting style loosely based?
Answer:The %-formatting style in Python is loosely based on the printf-style 
formatting used in C and C++. 
_________________________________________________________________________
Write a Python program that uses a loop and the str.rjust() method to generate the
following output.
##########
#########
########
#######
######
#####
####
###
##
#
Hint: The program will start as follows
for n in range(10,0,-1):
line = "#" * n
# rest of code....
Answer:
for n in range(10,0,-1):
    line = "#" * n
    print(line.rjust(12))
_________________________________________________________________________
What is the basic element that all computer files contain?
Answer:Bit

_________________________________________________________________________
What function must be called before the contents of a file can be accessed?
Answer:open()
_________________________________________________________________________
What method must be called on a file object once processing is complete?
Answer:close()
_________________________________________________________________________
Following execution of the given statement, would the file ‘myfile.txt’ be open for
reading or for writing?
f = open("myfile.txt")
Answer:Yes, the file ‘myfile.txt’ would be open for writing.
_________________________________________________________________________
Following execution of the given statement, would the file yourfile.txt be open for
reading or for writing?
f2 = open("yourfile.txt", "w")
Answer: Open for writing
_________________________________________________________________________

Following execution of the given statement, what would be the mode of operation applied to
file gfxlib.so ?
f3 = open("gfxlib.so", "r+b")
Answer:This allows both reading and writing.
_________________________________________________________________________
What is the difference between the two following method calls?
f.readline()
f.readlines()
Answer:
f.readline() reads a single line from the file, while f.readlines() reads all 
the lines and returns them as a list of strings. So, one is for reading just one line, 
and the other is for grabbing the whole
_________________________________________________________________________
How much of the file content would be read with the following method call?
content = f.read()
Answer:It reads entire file at once.
_________________________________________________________________________
If the variable ‘my_file’ referred to a text file, what would the following code do?
for next in my_file:
print(next)
Answer:This code would loop through each line with the text file specified by the 
variable my_file. Each line in the loop would be represented by the variable next. 

_________________________________________________________________________
What is the issue with the following code? And how could it be fixed?
f = open("details.txt", "w")
total = 100
f.write(total)
f.close()
Answer:write() function expects a string as input but we are assigning integer.
_________________________________________________________________________
What is the purpose of the file tell() method?
Answer:To retrieve the current postition of file pointer.
_________________________________________________________________________
What does the following code do?
f.seek(0)
Answer:It is used to change the current postion of the file pointer.
_________________________________________________________________________
Why is file handling often done using a ‘with’ statement as shown below?
with open("data.txt") as f:
lines = f.readlines()
Answer:The with statement ensures that the file is automatically closed after use, 
reducing the risk of resource leaks.

